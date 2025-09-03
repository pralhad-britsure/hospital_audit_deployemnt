# src/api/hospital_api.py

from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date, datetime

from src.schema.case_details import HospitalResponse
from src.service.case_details import get_filtered_hospitals
from src.database import get_db

router = APIRouter(prefix="/hospital", tags=["Case details"])

# @router.get("/filter", response_model=List[HospitalResponse])
# def filter_hospitals(
#     employee_id: Optional[int] = Query(None),
#     received_date: Optional[date] = Query(None),
#     from_date: Optional[date] = Query(None),
#     to_date: Optional[date] = Query(None),
#     search: Optional[str] = Query(None),
#     db: Session = Depends(get_db)
# ):
#     # If no dates provided, default to today for daily filter
#     if not received_date and not (from_date and to_date):
#         received_date = datetime.today().date()
#
#     hospitals = get_filtered_hospitals(
#         db=db,
#         employee_id=employee_id,
#         from_date=from_date,
#         to_date=to_date,
#         received_date=received_date,
#         search=search
#     )
#
#     return hospitals

@router.get("/case-details-filter", response_model=List[HospitalResponse])
def filter_case_details(
    employee_id: Optional[int] = Query(None),
    received_date: Optional[date] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    search: Optional[str] = Query(None),
    daily: bool = Query(False),
    db: Session = Depends(get_db)
):
    if daily and not received_date and not (from_date and to_date):
        received_date = datetime.today().date()

    hospitals = get_filtered_hospitals(
        db=db,
        employee_id=employee_id,
        from_date=from_date,
        to_date=to_date,
        received_date=received_date,
        search=search
    )

    return hospitals
