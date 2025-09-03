from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum

class UserRole(str, Enum):
    super_admin = "super_admin"
    master = "master"
    data_entry_operator = "data_entry_operator"
    senior_manager = "senior_manager"
    auditor = "auditor"
    executive = "executive"
    field_officer = "field_officer"

class AccessType(str, Enum):
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


# Base Schema (shared fields)
class EmployeeBase(BaseModel):
    username: str
    EmployeeName: str
    MobileNo: Optional[str] = None
    PhoneNo: Optional[str] = None
    HomeAddress: Optional[str] = None
    State: Optional[str] = None
    District: Optional[str] = None
    Taluka: Optional[str] = None
    City: Optional[str] = None
    Area: Optional[str] = None
    Pin: Optional[str] = None
    EmailAddress: EmailStr
    Designation: Optional[str] = None
    role: UserRole
    access: Optional[str] = None


class EmployeeUpdate(BaseModel):
    EmployeeName: Optional[str] = None
    MobileNo: Optional[str] = None
    PhoneNo: Optional[str] = None
    HomeAddress: Optional[str] = None
    State: Optional[str] = None
    District: Optional[str] = None
    Taluka: Optional[str] = None
    City: Optional[str] = None
    Area: Optional[str] = None
    Pin: Optional[str] = None
    Designation: Optional[str] = None
    role: Optional[UserRole] = None
    access: Optional[str] = None
    is_active: Optional[bool] = None


# Response Schema
class EmployeeResponse(EmployeeBase):
    EmployeeID: int
    is_active: Optional[bool] = None
    access_list: List[AccessType] = []

    class Config:
        from_attributes = True
