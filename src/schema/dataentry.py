from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class HospitalBulkEntryCreate(BaseModel):
    hospital_name: str
    address: str
    location_city: str
    state: str
    Dist: str
    Taluka: str


class HospitalCreate(BaseModel):
    hospital_name: str
    address: str
    location_city: str
    state: str
    Dist: str
    Taluka: str
    senior_manager: int
    executive: int
    data_entry_operator: int

class HospitalResponse(BaseModel):
    id: int
    hospital_name: str
    class Config:
        from_attributes = True

class HospitalCreatedResponse(BaseModel):
    message: str
    hospital: HospitalResponse
