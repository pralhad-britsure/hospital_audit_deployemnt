from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date
from src.database import get_db
from src.schema.get_all_reports import HospitalGetAllResponse
from src.service.get_all_reports import get_filtered_hospitals

router = APIRouter(prefix="/hospital", tags=["Get all Hospital Data"])
@router.get("/list", response_model=List[HospitalGetAllResponse])
def list_hospitals(
    hospital_name: Optional[str] = Query(None),
    address: Optional[str] = Query(None),
    location_city: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
    received_date: Optional[date] = Query(None),
    closed_date: Optional[date] = Query(None),
    visit_date: Optional[date] = Query(None),
    senior_manager: Optional[int] = Query(None),
    executive: Optional[int] = Query(None),
    fo: Optional[int] = Query(None),
    visit_status: Optional[str] = Query(None),
    visit_remark: Optional[str] = Query(None),
    audit_status: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    Dist: Optional[str] = Query(None),
    Taluka: Optional[str] = Query(None),
    data_entry_operator: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    hospitals = get_filtered_hospitals(
        db=db,
        hospital_name=hospital_name,
        address=address,
        location_city=location_city,
        state=state,
        received_date=received_date,
        closed_date=closed_date,
        visit_date=visit_date,
        senior_manager=senior_manager,
        executive=executive,
        fo=fo,
        visit_status=visit_status,
        visit_remark=visit_remark,
        audit_status=audit_status,
        status=status,
        Dist=Dist,
        Taluka=Taluka,
        data_entry_operator=data_entry_operator
    )
    return hospitals