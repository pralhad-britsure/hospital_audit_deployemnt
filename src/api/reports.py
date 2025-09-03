from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from typing import List
from datetime import date

from src.service.reports import get_hospital_data_from_proc, export_hospitals_to_excel, export_hospitals_to_docx_zip
from src.database import get_db
from datetime import date
from typing import Optional
#from src.model.dataentry import Hospital
#from src.schema.reports import HospitalFullResponse
from src.schema.reports import FullHospitalDataList
from fastapi import Query
from datetime import datetime

router = APIRouter(prefix="/hospital", tags=["reposrts"])

def parse_date(date_str: Optional[str]) -> Optional[date]:
    try:
        if date_str:
            return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None
    return None

@router.get("/hospitals-not-working", response_model=FullHospitalDataList)
def get_hospitals(
    hospital_id: Optional[int] = Query(None),
    state: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    district: Optional[str] = Query(None),
    taluka: Optional[str] = Query(None),
    from_date: Optional[str] = Query(None),
    too_date: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    from_date_parsed = parse_date(from_date)
    to_datee_parsed = parse_date(too_date)

    hospitals = get_hospital_data_from_proc(
        db,
        hospital_id=hospital_id,
        state=state,
        city=city,
        district=district,
        taluka=taluka,
        from_date=from_date_parsed,
        to_date=to_datee_parsed,
    )
    return {"hospitals": hospitals}



@router.get("/hospitals/report-export")
def export_hospital_excel(
    hospital_id: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    district: Optional[str] = Query(None),
    taluka: Optional[str] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    hospitals = get_hospital_data_from_proc(
        db,
        hospital_id=hospital_id,
        state=state,
        city=city,
        district=district,
        taluka=taluka,
        from_date=from_date,
        to_date=to_date,
    )
    return export_hospitals_to_excel(hospitals)


@router.get("/hospitals/report-export-docs")
def export_hospital_docs(
    hospital_id: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    district: Optional[str] = Query(None),
    taluka: Optional[str] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    hospitals = get_hospital_data_from_proc(
        db,
        hospital_id=hospital_id,
        state=state,
        city=city,
        district=district,
        taluka=taluka,
        from_date=from_date,
        to_date=to_date,
    )
    return export_hospitals_to_docx_zip(hospitals)
