from pydantic import BaseModel, EmailStr
from typing import Optional
from src.model.user import UserRole

class UserBase(BaseModel):
    username: str
    EmailAddress: EmailStr
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
    access: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: Optional[UserRole] = UserRole.field_officer

class UserLogin(BaseModel):
    EmailAddress: EmailStr
    password: str

class UserResponse(UserBase):
    EmployeeID: int
    role: UserRole
    access: Optional[str] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    access: Optional[str] = None
    EmployeeID: int


class EmployeeSimpleResponse(BaseModel):
    EmployeeID: int
    EmployeeName: str

    class Config:
        from_attributes = True



class HospitalEmployeeResponse(BaseModel):
    hospital_id: int
    hospital_name: str
    fo_name: Optional[str]
    senior_manager_name: Optional[str]
    executive_name: Optional[str]

    class Config:
        from_attributes = True
