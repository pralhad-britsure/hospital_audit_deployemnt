from pydantic import BaseModel

class EmailRequest(BaseModel):
    employee_id: int
    hospital_name: str
    address: str
    city: str
    taluka: str
    district: str
