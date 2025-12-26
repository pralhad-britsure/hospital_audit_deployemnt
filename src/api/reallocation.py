# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
#
# from src.database import get_db
# from src.service.reallocation import mark_hospital_completed, reallocate_hospital
# from src.schema.reallocation import HospitalUpdateStatus,HospitalResponse, HospitalReallocate
#
#
# router = APIRouter(prefix="/hospital", tags=["Reallocation"])
#
# @router.post("/mark-completed", response_model=HospitalResponse)
# def mark_completed(request: HospitalUpdateStatus, db: Session = Depends(get_db)):
#     hospital = mark_hospital_completed(db, request.id)
#     if not hospital:
#         raise HTTPException(status_code=404, detail="Hospital not found")
#     return hospital
#
# @router.post("/reallocate", response_model=HospitalResponse)
# def reallocate(request: HospitalReallocate, db: Session = Depends(get_db)):
#     hospital = reallocate_hospital(db, request.id)
#     if not hospital:
#         raise HTTPException(status_code=404, detail="Hospital not found")
#     return hospital


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.service.reallocation import mark_hospital_completed, reallocate_hospital
from src.schema.reallocation import HospitalUpdateStatus, HospitalReallocate, HospitalActionResponse

router = APIRouter(prefix="/hospital", tags=["Reallocation"])


@router.post("/mark-completed", response_model=HospitalActionResponse)
def mark_completed(request: HospitalUpdateStatus, db: Session = Depends(get_db)):
    hospital = mark_hospital_completed(db, request.id)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital


@router.post("/reallocate", response_model=HospitalActionResponse)
def reallocate(request: HospitalReallocate, db: Session = Depends(get_db)):
    hospital = reallocate_hospital(db, request.id)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital
