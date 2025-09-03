from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP, func
from sqlalchemy.orm import relationship

from src.database import Base


class Hospital(Base):
    __tablename__ = 'hospital'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hospital_name = Column(String(255))
    address = Column(Text)
    location_city = Column(String(100))
    state = Column(String(50))
    received_date = Column(TIMESTAMP, server_default=func.now())
    closed_date = Column(Date)
    visit_date = Column(Date)
    senior_manager = Column(Integer)
    executive = Column(Integer)
    fo = Column(Integer)
    visit_status = Column(String(50))
    visit_remark = Column(Text)
    audit_status = Column(String(50))
    status = Column(String(50))
    Dist = Column(String(50))
    Taluka = Column(String(50))
    data_entry_operator = Column(Integer)

    basic_info = relationship("BasicInfo", back_populates="hospital",uselist=False)
    registration_details = relationship("RegistrationDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    empanelment_details = relationship("EmpanelmentDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    staff_details = relationship("StaffDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    infrastructure_details = relationship("InfrastructureDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    lab_details = relationship("LabDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    registers_protocols = relationship("RegistersProtocols", back_populates="hospital", cascade="all, delete",uselist=False)
    pharmacy_details = relationship("PharmacyDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    bagic_details = relationship("BagicDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    financial_details = relationship("FinancialDetails", back_populates="hospital", cascade="all, delete",uselist=False)
    audit_metadata = relationship("AuditMetadata", back_populates="hospital", cascade="all, delete", uselist=False)
