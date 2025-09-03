import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UserRole(str, enum.Enum):
    super_admin = "super_admin"
    master = "master"
    data_entry_operator = "data_entry_operator"
    senior_manager = "senior_manager"
    auditor = "auditor"
    executive = "executive"
    field_officer = "field_officer"

class AccessType(str, enum.Enum):
    data_entry = "data_entry"
    allocation = "allocation"
    operation = "operation"
    closure = "closure"
    completed_reports = "completed_reports"
    data_entry_reports = "data_entry_reports"
    status_wise_reports = "status_wise_reports"
    fo_wise_reports = "fo_wise_reports"
    executive_wise_reports = "executive_wise_reports"
    employee_master = "employee_master"
    user_access_management = "user_access_management"
    reports = "reports"


user_access_association = Table(
    "user_access_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("employee_master.EmployeeID")),
    Column("access_type", Enum(AccessType, name="access_enum"))
)

class Employee(Base):
    __tablename__ = "employee_master"

    EmployeeID = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    EmployeeName = Column(String)
    MobileNo = Column(String)
    PhoneNo = Column(String)
    HomeAddress = Column(String)
    State = Column(String)
    District = Column(String)
    Taluka = Column(String)
    City = Column(String)
    Area = Column(String)
    Pin = Column(String)
    EmailAddress = Column(String, unique=True)
    hashed_password = Column(String)
    Designation = Column(String)
    role = Column(Enum(UserRole), nullable=False)
    access = Column(String)

    is_active = Column(Boolean, default=True)

    #access = relationship("AccessType",secondary=user_access_association,viewonly=True,lazy='joined')
