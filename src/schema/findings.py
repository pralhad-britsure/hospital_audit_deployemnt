from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class HospitalUpdateVisit(BaseModel):
    visit_date: date
    fo_id: int


class HospitalOut(BaseModel):
    id: int
    hospital_name: Optional[str]
    address: Optional[str]
    location_city: Optional[str]
    state: Optional[str]
    received_date: Optional[datetime]
    closed_date: Optional[date]
    visit_date: Optional[date]
    senior_manager: Optional[int]
    senior_manager_name: Optional[str]
    executive: Optional[int]
    executive_name: Optional[str]
    fo: Optional[int]
    fo_name: Optional[str]
    visit_status: Optional[str]
    visit_remark: Optional[str]
    audit_status: Optional[str]
    status: Optional[str]
    Dist: Optional[str]
    Taluka: Optional[str]
    data_entry_operator: Optional[int]

    class Config:
        from_attributes = True

class UpdateVisitInfoRequest(BaseModel):
    hospital_id: int
    visit_status: Optional[str]
    visit_remark: Optional[str]
