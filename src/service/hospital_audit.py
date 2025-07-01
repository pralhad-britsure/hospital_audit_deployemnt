# from sqlalchemy.orm import Session
# from sqlalchemy import and_, or_
# from typing import List, Optional
# from src.models.hospital_audit import HospitalAudit
# from src.schema.hospital_audit import HospitalAuditCreate, HospitalAuditUpdate
#
#
# class HospitalAuditService:
#     def __init__(self, db: Session):
#         self.db = db
#
#     def create_hospital_audit(self, audit_data: HospitalAuditCreate) -> HospitalAudit:
#         """Create a new hospital audit record"""
#         db_audit = HospitalAudit(**audit_data.dict())
#         self.db.add(db_audit)
#         self.db.commit()
#         self.db.refresh(db_audit)
#         return db_audit
#
#     def get_hospital_audit_by_id(self, hosp_id: int) -> Optional[HospitalAudit]:
#         """Get hospital audit by ID"""
#         return self.db.query(HospitalAudit).filter(HospitalAudit.hosp_id == hosp_id).first()
#
#     def get_all_hospital_audits(
#             self,
#             skip: int = 0,
#             limit: int = 100,
#             state: Optional[str] = None,
#             hospital_type: Optional[str] = None,
#             area_type: Optional[str] = None
#     ) -> List[HospitalAudit]:
#         """Get all hospital audits with optional filters"""
#         query = self.db.query(HospitalAudit)
#
#         if state:
#             query = query.filter(HospitalAudit.state == state)
#         if hospital_type:
#             query = query.filter(HospitalAudit.hospital_type == hospital_type)
#         if area_type:
#             query = query.filter(HospitalAudit.area_type == area_type)
#
#         return query.offset(skip).limit(limit).all()
#
#     def search_hospitals(
#             self,
#             search_term: str,
#             skip: int = 0,
#             limit: int = 100
#     ) -> List[HospitalAudit]:
#         """Search hospitals by name, city, or address"""
#         return self.db.query(HospitalAudit).filter(
#             or_(
#                 HospitalAudit.hospital_name.ilike(f"%{search_term}%"),
#                 HospitalAudit.location_city.ilike(f"%{search_term}%"),
#                 HospitalAudit.address.ilike(f"%{search_term}%")
#             )
#         ).offset(skip).limit(limit).all()
#
#     def update_hospital_audit(
#             self,
#             hosp_id: int,
#             audit_data: HospitalAuditUpdate
#     ) -> Optional[HospitalAudit]:
#         """Update hospital audit record"""
#         db_audit = self.get_hospital_audit_by_id(hosp_id)
#         if not db_audit:
#             return None
#
#         update_data = audit_data.dict(exclude_unset=True)
#         for field, value in update_data.items():
#             setattr(db_audit, field, value)
#
#         self.db.commit()
#         self.db.refresh(db_audit)
#         return db_audit
#
#     def delete_hospital_audit(self, hosp_id: int) -> bool:
#         """Delete hospital audit record"""
#         db_audit = self.get_hospital_audit_by_id(hosp_id)
#         if not db_audit:
#             return False
#
#         self.db.delete(db_audit)
#         self.db.commit()
#         return True
#
#     def get_audit_count(self) -> int:
#         """Get total count of audit records"""
#         return self.db.query(HospitalAudit).count()
#
#     def get_audits_by_state(self, state: str) -> List[HospitalAudit]:
#         """Get all audits for a specific state"""
#         return self.db.query(HospitalAudit).filter(HospitalAudit.state == state).all()


from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from src.models.hospital_audit import HospitalAudit
from src.schema.hospital_audit import HospitalAuditCreate, HospitalAuditUpdate
from src.enum import StateEnum, AreaTypeEnum, HospitalTypeEnum  # Import your enums


class HospitalAuditService:
    def __init__(self, db: Session):
        self.db = db

    def validate_enum_fields(self, audit_data: HospitalAuditCreate):
        """Validate enum fields before database insertion"""
        errors = []

        # Validate state
        if audit_data.state:
            try:
                StateEnum(audit_data.state)
            except ValueError:
                valid_states = [e.value for e in StateEnum]
                errors.append(f"Invalid state '{audit_data.state}'. Valid values: {valid_states}")

        # Validate area_type
        if audit_data.area_type:
            try:
                AreaTypeEnum(audit_data.area_type)
            except ValueError:
                valid_area_types = [e.value for e in AreaTypeEnum]
                errors.append(f"Invalid area_type '{audit_data.area_type}'. Valid values: {valid_area_types}")

        # Add more enum validations as needed

        if errors:
            raise ValueError("; ".join(errors))

    def create_hospital_audit(self, audit_data: HospitalAuditCreate) -> HospitalAudit:
        """Create a new hospital audit record with validation"""
        try:
            # Validate enum fields first
            self.validate_enum_fields(audit_data)

            db_audit = HospitalAudit(**audit_data.dict())
            self.db.add(db_audit)
            self.db.commit()
            self.db.refresh(db_audit)
            return db_audit

        except ValueError as ve:
            raise ValueError(f"Validation error: {str(ve)}")
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Database error: {str(e)}")

    def get_hospital_audit_by_id(self, hosp_id: int) -> Optional[HospitalAudit]:
        """Get hospital audit by ID"""
        return self.db.query(HospitalAudit).filter(HospitalAudit.hosp_id == hosp_id).first()

    def get_all_hospital_audits(
            self,
            skip: int = 0,
            limit: int = 100,
            state: Optional[str] = None,
            hospital_type: Optional[str] = None,
            area_type: Optional[str] = None
    ) -> List[HospitalAudit]:
        """Get all hospital audits with optional filters"""
        query = self.db.query(HospitalAudit)

        if state:
            query = query.filter(HospitalAudit.state == state)
        if hospital_type:
            query = query.filter(HospitalAudit.hospital_type == hospital_type)
        if area_type:
            query = query.filter(HospitalAudit.area_type == area_type)

        return query.offset(skip).limit(limit).all()

    def search_hospitals(
            self,
            search_term: str,
            skip: int = 0,
            limit: int = 100
    ) -> List[HospitalAudit]:
        """Search hospitals by name, city, or address"""
        return self.db.query(HospitalAudit).filter(
            or_(
                HospitalAudit.hospital_name.ilike(f"%{search_term}%"),
                HospitalAudit.location_city.ilike(f"%{search_term}%"),
                HospitalAudit.address.ilike(f"%{search_term}%")
            )
        ).offset(skip).limit(limit).all()

    def update_hospital_audit(
            self,
            hosp_id: int,
            audit_data: HospitalAuditUpdate
    ) -> Optional[HospitalAudit]:
        """Update hospital audit record"""
        db_audit = self.get_hospital_audit_by_id(hosp_id)
        if not db_audit:
            return None

        update_data = audit_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_audit, field, value)

        self.db.commit()
        self.db.refresh(db_audit)
        return db_audit

    def delete_hospital_audit(self, hosp_id: int) -> bool:
        """Delete hospital audit record"""
        db_audit = self.get_hospital_audit_by_id(hosp_id)
        if not db_audit:
            return False

        self.db.delete(db_audit)
        self.db.commit()
        return True

    def get_audit_count(self) -> int:
        """Get total count of audit records"""
        return self.db.query(HospitalAudit).count()

    def get_audits_by_state(self, state: str) -> List[HospitalAudit]:
        """Get all audits for a specific state"""
        return self.db.query(HospitalAudit).filter(HospitalAudit.state == state).all()