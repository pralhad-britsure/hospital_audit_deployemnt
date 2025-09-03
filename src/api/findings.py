from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schema.findings import HospitalUpdateVisit
from src.service.findings import update_visit_details
from typing import List
from src.schema.findings import HospitalOut
from src.service.findings import get_hospitals_by_fo_and_status


router = APIRouter(prefix="/hospital", tags=["Findings"])

@router.put("/update-visit/{hospital_id}")
def update_hospital_visit(
    hospital_id: int,
    visit_update: HospitalUpdateVisit,
    db: Session = Depends(get_db)
):
    return update_visit_details(db, hospital_id, visit_update)


@router.get("/fo_id_finding/{fo_id}", response_model=List[HospitalOut])
def get_hospitals_by_fo(fo_id: int, db: Session = Depends(get_db)):
    hospitals = get_hospitals_by_fo_and_status(db, fo_id)
    if not hospitals:
        raise HTTPException(status_code=404, detail="No hospitals found with given FO ID and 'findings' status.")
    return hospitals


from src.schema.findings import UpdateVisitInfoRequest
from src.service.findings import update_visit_info


@router.put("/update-visit-info", response_model=UpdateVisitInfoRequest)
def update_visit_info_api(data: UpdateVisitInfoRequest, db: Session = Depends(get_db)):
    result = update_visit_info(db, data)
    if not result:
        raise HTTPException(status_code=404, detail="Hospital not found.")
    return result