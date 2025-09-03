from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schema.dataentry import HospitalCreate, HospitalResponse, HospitalBulkEntryCreate
from src.service.dataentry import create_hospital, bulk_create_hospitals
import pandas as pd
import io
from fastapi import Form
from src.schema.dataentry import HospitalCreatedResponse

router = APIRouter(prefix="/hospital", tags=["Data Entry"])


@router.post("/data-entry-upload-excel")
async def upload_excel(
        senior_manager: int = Form(...),
        executive: int = Form(...),
        data_entry_operator: int = Form(...),
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    try:
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        expected_cols = {'hospital_name', 'address', 'location_city', 'state', 'Dist', 'Taluka'}
        if not expected_cols.issubset(df.columns):
            raise HTTPException(status_code=400, detail="Invalid Excel format. Required columns missing.")

        hospitals = [
            HospitalBulkEntryCreate(**row.dropna().to_dict())
            for _, row in df.iterrows()
        ]
        result = bulk_create_hospitals(db, hospitals, senior_manager, executive, data_entry_operator)
        return {"status": "success", "detail": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/data-entry", response_model=HospitalCreatedResponse, status_code=201)
def create_single_hospital(hospital: HospitalCreate, db: Session = Depends(get_db)):
    try:
        hospital_obj = create_hospital(db, hospital)
        return {
            "message": "Hospital created successfully",
            "hospital": hospital_obj
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))