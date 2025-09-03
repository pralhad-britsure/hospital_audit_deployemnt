import os
import io
import zipfile
import paramiko
from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI, Form, UploadFile, File, APIRouter
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse

from src.sftp import upload_file_to_sftp

load_dotenv()

router = APIRouter(prefix="/hospital", tags=["SFTP"])

SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_USERNAME = os.getenv("SFTP_USERNAME")
SFTP_PASSWORD = os.getenv("SFTP_PASSWORD")
SFTP_BASE_PATH = os.getenv("SFTP_BASE_PATH")

router = APIRouter()

CATEGORY_LIST = [
    "Basic Information",
    "Schemes & Empanelments",
    "Registrations & Certifications",
    "Key Personnel & Staff Details",
    "Infrastructure",
    "Laboratory Information & Diagnostic Equipment",
    "Pharmacy Information",
    "Records & Compliance",
    "BAGIC Specific",
    "Audit Information"
]

ALLOWED_EXTENSIONS = {
    # Documents
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "odt", "rtf", "md", "csv",
    # Images
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg", "ico",
    # Videos
    "mp4", "mkv", "mov", "avi", "flv", "wmv", "webm", "3gp", "mpeg",
    # Audio
    "mp3", "wav", "aac", "ogg", "flac", "m4a", "wma",
    # Archives & Compressed
    "zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso",
    # Legacy/misc
    "xl", "hd"
}

def is_allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS


@router.post("/upload-document/")
async def upload_images(
        hospital_id : str = Form(...),
        category: str = Form(...),
        files: List[UploadFile] = File(...)
):
    result = []

    if category not in CATEGORY_LIST:
        return JSONResponse(status_code=400, content={"error": f"Invalid category: {category}"})

    for file in files:
        if not is_allowed_file(file.filename):
            result.append({
                "file": file.filename,
                "category": category,
                "status": "failed - unsupported file format"
            })
            continue

        file_data = await file.read()
        remote_path = os.path.join(
            os.getenv("SFTP_BASE_PATH", "/Data_Source/Test"),
            hospital_id ,
            category,
            file.filename
        ).replace("\\", "/")

        try:
            upload_file_to_sftp(file_data, remote_path)
            result.append({
                "file": file.filename,
                "category": category,
                "status": "uploaded",
                "path": remote_path
            })
        except Exception as e:
            result.append({
                "file": file.filename,
                "category": category,
                "status": f"failed - {str(e)}"
            })

    return {"uploaded_files": result}


@router.get("/download-hospital-documents/")
def download_hospital_documents(hospital_id: str):
    base_path = os.getenv("SFTP_BASE_PATH", "/Data_Source/Test")
    hospital_path = os.path.join(base_path, hospital_id).replace("\\", "/")

    memory_file = io.BytesIO()

    try:
        # Connect to SFTP
        transport = paramiko.Transport((SFTP_HOST, 22))
        transport.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)

        with zipfile.ZipFile(memory_file, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            for category in CATEGORY_LIST:
                category_path = f"{hospital_path}/{category}"
                try:
                    file_list = sftp.listdir(category_path)
                    for file_name in file_list:
                        file_path = f"{category_path}/{file_name}"
                        with sftp.file(file_path, 'rb') as f:
                            file_content = f.read()
                            zip_internal_path = f"{category}/{file_name}"
                            zf.writestr(zip_internal_path, file_content)
                except IOError:
                    # Skip if the folder does not exist
                    continue

        sftp.close()
        transport.close()

        memory_file.seek(0)
        return StreamingResponse(memory_file, media_type="application/x-zip-compressed", headers={
            "Content-Disposition": f"attachment; filename=hospital_{hospital_id}_documents.zip"
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
