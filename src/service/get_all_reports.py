from sqlalchemy.orm import Session
from sqlalchemy import and_
from src.model.dataentry import Hospital
from typing import Optional
from datetime import date

def get_filtered_hospitals(
    db: Session,
    hospital_name: Optional[str] = None,
    address: Optional[str] = None,
    location_city: Optional[str] = None,
    state: Optional[str] = None,
    received_date: Optional[date] = None,
    closed_date: Optional[date] = None,
    visit_date: Optional[date] = None,
    senior_manager: Optional[int] = None,
    executive: Optional[int] = None,
    fo: Optional[int] = None,
    visit_status: Optional[str] = None,
    visit_remark: Optional[str] = None,
    audit_status: Optional[str] = None,
    status: Optional[str] = None,
    Dist: Optional[str] = None,
    Taluka: Optional[str] = None,
    data_entry_operator: Optional[int] = None
):
    filters = []

    if hospital_name:
        filters.append(Hospital.hospital_name == hospital_name)
    if address:
        filters.append(Hospital.address == address)
    if location_city:
        filters.append(Hospital.location_city == location_city)
    if state:
        filters.append(Hospital.state == state)
    if received_date:
        filters.append(Hospital.received_date.cast(date) == received_date)
    if closed_date:
        filters.append(Hospital.closed_date == closed_date)
    if visit_date:
        filters.append(Hospital.visit_date == visit_date)
    if senior_manager is not None:
        filters.append(Hospital.senior_manager == senior_manager)
    if executive is not None:
        filters.append(Hospital.executive == executive)
    if fo is not None:
        filters.append(Hospital.fo == fo)
    if visit_status:
        filters.append(Hospital.visit_status == visit_status)
    if visit_remark:
        filters.append(Hospital.visit_remark == visit_remark)
    if audit_status:
        filters.append(Hospital.audit_status == audit_status)
    if status:
        filters.append(Hospital.status == status)
    if Dist:
        filters.append(Hospital.Dist == Dist)
    if Taluka:
        filters.append(Hospital.Taluka == Taluka)
    if data_entry_operator is not None:
        filters.append(Hospital.data_entry_operator == data_entry_operator)

    return db.query(Hospital).filter(and_(*filters)).all()
