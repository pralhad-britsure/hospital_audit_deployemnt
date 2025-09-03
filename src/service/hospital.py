from sqlalchemy.orm import Session
from src.model.hospital import BasicInfo
from src.schema.hospital import BasicInfoBase
from src.schema.hospital import RegistrationCreate
from src.model.hospital import RegistrationDetails
from src.schema.hospital import EmpanelmentCreate
from src.model.hospital import EmpanelmentDetails
from src.schema.hospital import StaffCreate
from src.model.hospital import StaffDetails
from src.schema.hospital import InfrastructureCreate
from src.model.hospital import InfrastructureDetails
from src.schema.hospital import LabCreate
from src.model.hospital import LabDetails
from src.schema.hospital import PharmacyCreate
from src.model.hospital import PharmacyDetails
from src.schema.hospital import RegistersProtocolsCreate
from src.model.hospital import RegistersProtocols
from src.schema.hospital import FinancialCreate
from src.model.hospital import FinancialDetails
from src.schema.hospital import BagicCreate
from src.model.hospital import BagicDetails
# from src.schema.hospital import DigitalEvidenceCreate
# from src.model.hospital import DigitalEvidence
from src.schema.hospital import AuditMetadataBase
from src.model.hospital import AuditMetadata

from src.repository.hospital_repository import get_full_hospital_data_by_id
from src.schema.hospital import FullHospitalData

def create_hospital(db: Session, hospital_data: BasicInfoBase):
    existing_info = db.query(BasicInfo).filter(BasicInfo.hospital_id == hospital_data.hospital_id).first()
    if existing_info:

        for key, value in hospital_data.dict(exclude_unset=True).items():
            setattr(existing_info, key, value)
        db.commit()
        db.refresh(existing_info)
        return existing_info
    else:
        new_hospital = BasicInfo(**hospital_data.dict())
        db.add(new_hospital)
        db.commit()
        db.refresh(new_hospital)
        return new_hospital


def create_registration_details(db: Session, data: RegistrationCreate):
    existing = db.query(RegistrationDetails).filter(RegistrationDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        new_entry = RegistrationDetails(**data.dict())
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry


def create_empanelment_details(db: Session, data: EmpanelmentCreate):
    existing = db.query(EmpanelmentDetails).filter(EmpanelmentDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        empanelment = EmpanelmentDetails(**data.dict())
        db.add(empanelment)
        db.commit()
        db.refresh(empanelment)
        return empanelment


def create_staff_details(db: Session, data: StaffCreate):
    existing = db.query(StaffDetails).filter(StaffDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        staff = StaffDetails(**data.dict())
        db.add(staff)
        db.commit()
        db.refresh(staff)
        return staff

def create_infrastructure_details(db: Session, data: InfrastructureCreate):
    existing = db.query(InfrastructureDetails).filter(InfrastructureDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        infra = InfrastructureDetails(**data.dict())
        db.add(infra)
        db.commit()
        db.refresh(infra)
        return infra


def create_lab_details(db: Session, data: LabCreate):
    existing = db.query(LabDetails).filter(LabDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        lab = LabDetails(**data.dict())
        db.add(lab)
        db.commit()
        db.refresh(lab)
        return lab

def create_pharmacy_details(db: Session, data: PharmacyCreate):
    existing = db.query(PharmacyDetails).filter(PharmacyDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        pharmacy = PharmacyDetails(**data.dict())
        db.add(pharmacy)
        db.commit()
        db.refresh(pharmacy)
        return pharmacy


def create_registers_protocols(db: Session, data: RegistersProtocolsCreate):
    existing = db.query(RegistersProtocols).filter(RegistersProtocols.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        record = RegistersProtocols(**data.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

def create_financial_details(db: Session, data: FinancialCreate):
    existing = db.query(FinancialDetails).filter(FinancialDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        record = FinancialDetails(**data.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record


def create_bagic_details(db: Session, data: BagicCreate):
    existing = db.query(BagicDetails).filter(BagicDetails.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        record = BagicDetails(**data.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record


# def create_digital_evidence(db: Session, data: DigitalEvidenceCreate):
#     record = DigitalEvidence(**data.dict())
#     db.add(record)
#     db.commit()
#     db.refresh(record)
#     return record

def create_audit_metadata_details(db: Session, data: AuditMetadataBase):
    existing = db.query(AuditMetadata).filter(AuditMetadata.hospital_id == data.hospital_id).first()
    if existing:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        record = AuditMetadata(**data.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

def fetch_hospital_with_all_sections(hospital_id: int, db: Session) -> FullHospitalData:
    hospital = get_full_hospital_data_by_id(db, hospital_id)

    if not hospital:
        return None

    return FullHospitalData(
    basic_info=BasicInfoBase.model_validate(hospital.basic_info) if hospital.basic_info else None,
    registration_details=RegistrationCreate.model_validate(hospital.registration_details) if hospital.registration_details else None,
    empanelment_details=EmpanelmentCreate.model_validate(hospital.empanelment_details) if hospital.empanelment_details else None,
    staff_details=StaffCreate.model_validate(hospital.staff_details) if hospital.staff_details else None,
    infra_structure_details=InfrastructureCreate.model_validate(hospital.infrastructure_details) if hospital.infrastructure_details else None,
    lab_details=LabCreate.model_validate(hospital.lab_details) if hospital.lab_details else None,
    pharmacy_details=PharmacyCreate.model_validate(hospital.pharmacy_details) if hospital.pharmacy_details else None,
    registers_protocol_details=RegistersProtocolsCreate.model_validate(hospital.registers_protocols) if hospital.registers_protocols else None,
    financial_details=FinancialCreate.model_validate(hospital.financial_details) if hospital.financial_details else None,
    bagic_details=BagicCreate.model_validate(hospital.bagic_details) if hospital.bagic_details else None,
    audit_metadata=AuditMetadataBase.model_validate(hospital.audit_metadata) if hospital.audit_metadata else None,
)