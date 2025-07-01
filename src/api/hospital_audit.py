from fastapi import FastAPI, Depends, HTTPException, Query, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from src.database import get_db
from src.schema.hospital_audit  import HospitalAuditCreate, HospitalAuditResponse, HospitalAuditUpdate
from src.service.hospital_audit import HospitalAuditService


router = APIRouter()

def get_hospital_service(db: Session = Depends(get_db)) -> HospitalAuditService:
    return HospitalAuditService(db)

@router.post("/api/hospital-audits", response_model=HospitalAuditResponse, status_code=201)
async def create_hospital_audit(
        audit_data: HospitalAuditCreate,
        service: HospitalAuditService = Depends(get_hospital_service)
):

    try:
        audit = service.create_hospital_audit(audit_data)
        return audit
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating audit: {str(e)}")

@router.get("/api/hospital-audits/{hosp_id}", response_model=HospitalAuditResponse)
async def get_hospital_audit(
        hosp_id: int,
        service: HospitalAuditService = Depends(get_hospital_service)
):
    audit = service.get_hospital_audit_by_id(hosp_id)
    if not audit:
        raise HTTPException(status_code=404, detail="Hospital audit not found")
    return audit

@router.get("/api/hospital-audits", response_model=List[HospitalAuditResponse])
async def get_all_hospital_audits(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
        state: Optional[str] = Query(None, description="Filter by state"),
        hospital_type: Optional[str] = Query(None, description="Filter by hospital type"),
        area_type: Optional[str] = Query(None, description="Filter by area type"),
        service: HospitalAuditService = Depends(get_hospital_service)
):
    """Get all hospital audits with optional filters"""
    audits = service.get_all_hospital_audits(
        skip=skip,
        limit=limit,
        state=state,
        hospital_type=hospital_type,
        area_type=area_type
    )
    return audits

@router.get("/api/hospital-audits/search", response_model=List[HospitalAuditResponse])
async def search_hospital_audits(
        q: str = Query(..., min_length=1, description="Search term"),
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=1000),
        service: HospitalAuditService = Depends(get_hospital_service)
):

    audits = service.search_hospitals(search_term=q, skip=skip, limit=limit)
    return audits

@router.put("/api/hospital-audits/{hosp_id}", response_model=HospitalAuditResponse)
async def update_hospital_audit(
        hosp_id: int,
        audit_data: HospitalAuditUpdate,
        service: HospitalAuditService = Depends(get_hospital_service)
):
    audit = service.update_hospital_audit(hosp_id, audit_data)
    if not audit:
        raise HTTPException(status_code=404, detail="Hospital audit not found")
    return audit

@router.delete("/api/hospital-audits/{hosp_id}", status_code=204)
async def delete_hospital_audit(
        hosp_id: int,
        service: HospitalAuditService = Depends(get_hospital_service)
):
    success = service.delete_hospital_audit(hosp_id)
    if not success:
        raise HTTPException(status_code=404, detail="Hospital audit not found")

@router.get("/api/hospital-audits/stats/count")
async def get_audit_count(
        service: HospitalAuditService = Depends(get_hospital_service)
):
    count = service.get_audit_count()
    return {"total_audits": count}

@router.get("/api/hospital-audits/by-state/{state}", response_model=List[HospitalAuditResponse])
async def get_audits_by_state(
        state: str,
        service: HospitalAuditService = Depends(get_hospital_service)
):
    audits = service.get_audits_by_state(state)
    return audits
