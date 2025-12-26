# from pydantic import BaseModel
# from typing import Optional
# from datetime import date, datetime
#
# class HospitalBase(BaseModel):
#     hospital_name: Optional[str]
#     address: Optional[str]
#     location_city: Optional[str]
#     state: Optional[str]
#     received_date: Optional[datetime]
#     closed_date: Optional[date]
#     visit_date: Optional[date]
#     senior_manager: Optional[int]
#     executive: Optional[int]
#     fo: Optional[int]
#     visit_status: Optional[str]
#     visit_remark: Optional[str]
#     audit_status: Optional[str]
#     status: Optional[str]
#     Dist: Optional[str]
#     Taluka: Optional[str]
#     data_entry_operator: Optional[int]
#
#     class Config:
#         from_attributes = True
#
# class HospitalResponse(HospitalBase):
#     id: int
#
# class HospitalUpdateStatus(BaseModel):
#     id: int
#
# class HospitalReallocate(BaseModel):
#     id: int


from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

# Base model (if you still need it elsewhere)
class HospitalBase(BaseModel):
    hospital_name: Optional[str]
    address: Optional[str]
    location_city: Optional[str]
    state: Optional[str]
    received_date: Optional[datetime]
    closed_date: Optional[date]
    visit_date: Optional[date]
    senior_manager: Optional[int]
    executive: Optional[int]
    fo: Optional[int]
    visit_status: Optional[str]
    visit_remark: Optional[str]
    audit_status: Optional[str]
    status: Optional[str]
    Dist: Optional[str]
    Taluka: Optional[str]
    data_entry_operator: Optional[int]

    class Config:
        from_attributes = True


# Request schemas
class HospitalUpdateStatus(BaseModel):
    id: int


class HospitalReallocate(BaseModel):
    id: int


# Response schema (only what you want to return)
class HospitalActionResponse(BaseModel):
    id: int
    status: str

