from fastapi import FastAPI, Form, UploadFile, File, APIRouter
from fastapi.responses import JSONResponse
from typing import List
import os
from src.sftp import upload_file_to_sftp

router = APIRouter()

CATEGORY_LIST = [
    "Basic Information",
    "Schemes & Empanelments",
    "Registrations & Certifications",
    "Key Personnel",
    "Staff Details",
    "Infrastructure",
    "Laboratory Information",
    "Diagnostic Equipment",
    "Pharmacy Information",
    "Records & Compliance",
    "BAGIC Specific",
    "Audit Information"
]

# Allowed file extensions
ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png", "zip", "mp4", "mp3", "hd", "xlsx", "xl"}


def is_allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS


@router.post("/upload/")
async def upload_images(
        unique_code : str = Form(...),
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
            unique_code ,
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
