from datetime import date,datetime
from typing import Optional
from pydantic import BaseModel, field_serializer

class HospitalResponse(BaseModel):
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

    @field_serializer("received_date", when_used="always")
    def serialize_received_date(self, value: Optional[datetime], _info):
        return value.date().isoformat() if value else None
