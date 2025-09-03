from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schema.hospital import BasicInfoBase
from src.service.hospital import create_hospital
from src.database import get_db
import traceback

from src.service.hospital import create_registration_details
from src.schema.hospital import RegistrationCreate
from src.service.hospital import create_empanelment_details
from src.schema.hospital import EmpanelmentCreate
from src.service.hospital import create_staff_details
from src.schema.hospital import StaffCreate
from src.service.hospital import create_infrastructure_details
from src.schema.hospital import InfrastructureCreate
from src.service.hospital import create_lab_details
from src.schema.hospital import LabCreate
from src.service.hospital import create_pharmacy_details
from src.schema.hospital import PharmacyCreate
from src.service.hospital import create_registers_protocols
from src.schema.hospital import RegistersProtocolsCreate
from src.service.hospital import create_financial_details
from src.schema.hospital import FinancialCreate
from src.service.hospital import create_bagic_details
from src.schema.hospital import BagicCreate
# from src.service.hospital import create_digital_evidence
# from src.schema.hospital import DigitalEvidenceCreate
from src.service.hospital import create_audit_metadata_details
from src.schema.hospital import AuditMetadataBase
from src.schema.hospital import FullHospitalData
from src.service.hospital import fetch_hospital_with_all_sections


router = APIRouter(prefix="/hospital", tags=["Hospital"])

@router.post("/hospital-basic", status_code=201)
def create_hospital_api(hospital: BasicInfoBase, db: Session = Depends(get_db)):
    try:
        return create_hospital(db, hospital)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/registration-details", status_code=201)
def create_registration_api(data: RegistrationCreate, db: Session = Depends(get_db)):
    try:
        return create_registration_details(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/empanelment-details", status_code=201)
def create_empanelment_api(data: EmpanelmentCreate, db: Session = Depends(get_db)):
    try:
        return create_empanelment_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/staff-details", status_code=201)
def create_staff_api(data: StaffCreate, db: Session = Depends(get_db)):
    try:
        return create_staff_details(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/infrastructure-details", status_code=201)
def create_infrastructure_api(data: InfrastructureCreate, db: Session = Depends(get_db)):
    try:
        return create_infrastructure_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/lab-details", status_code=201)
def create_lab_api(data: LabCreate, db: Session = Depends(get_db)):
    try:
        return create_lab_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/pharmacy-details", status_code=201)
def create_pharmacy_api(data: PharmacyCreate, db: Session = Depends(get_db)):
    try:
        return create_pharmacy_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/registers-protocols-details", status_code=201)
def create_registers_protocols_api(data: RegistersProtocolsCreate, db: Session = Depends(get_db)):
    try:
        return create_registers_protocols(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/finacial_details", status_code=201)
def create_financial_api(data: FinancialCreate, db: Session = Depends(get_db)):
    try:
        return create_financial_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/bagic-details", status_code=201)
def create_bagic_api(data: BagicCreate, db: Session = Depends(get_db)):
    try:
        return create_bagic_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
#
# @router.post("/digital-evidance-details", status_code=201)
# def create_digital_evidance_api(data: DigitalEvidenceCreate, db: Session = Depends(get_db)):
#     try:
#         return create_digital_evidence(db, data)
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=str(e))

@router.post("/audit-metadata", status_code=201)
def create_audit_metadata_api(data: AuditMetadataBase, db: Session = Depends(get_db)):
    try:
        return create_audit_metadata_details(db, data)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/hospital/{hospital_id}/full", response_model=FullHospitalData)
def get_full_hospital_data(hospital_id: int, db: Session = Depends(get_db)):
    data = fetch_hospital_with_all_sections(hospital_id, db)
    if not data:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return data