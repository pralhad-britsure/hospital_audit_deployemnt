from sqlalchemy.orm import Session
from src.model.dataentry import Hospital
from src.schema.findings import HospitalUpdateVisit
from fastapi import HTTPException
from sqlalchemy.orm import aliased
from src.model.user import  Employee



def update_visit_details(db: Session, hospital_id: int, update_data: HospitalUpdateVisit):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()

    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")

    hospital.visit_date = update_data.visit_date
    hospital.fo = update_data.fo_id
    hospital.status = "findings"

    db.commit()
    db.refresh(hospital)

    return {"message": "Hospital visit details updated successfully", "hospital_id": hospital_id}
#
#
# def get_hospitals_by_fo_and_status(db: Session, fo_id: int):
#     return db.query(Hospital).filter(Hospital.fo == fo_id, Hospital.status == "findings").all()

def get_hospitals_by_fo_and_status(db: Session, fo_id: int):
    emp_sm = aliased(Employee)
    emp_ex = aliased(Employee)
    emp_fo = aliased(Employee)

    query = db.query(
        Hospital,
        emp_sm.EmployeeName.label("senior_manager_name"),
        emp_ex.EmployeeName.label("executive_name"),
        emp_fo.EmployeeName.label("fo_name")
    ).outerjoin(emp_sm, Hospital.senior_manager == emp_sm.EmployeeID
    ).outerjoin(emp_ex, Hospital.executive == emp_ex.EmployeeID
    ).outerjoin(emp_fo, Hospital.fo == emp_fo.EmployeeID
    ).filter(
        Hospital.fo == fo_id,
        Hospital.status == "findings"
    )

    results = query.all()

    response = []
    for hospital, sm_name, ex_name, fo_name in results:
        hospital_dict = hospital.__dict__.copy()
        hospital_dict["senior_manager_name"] = sm_name
        hospital_dict["executive_name"] = ex_name
        hospital_dict["fo_name"] = fo_name
        response.append(hospital_dict)

    return response

from sqlalchemy.orm import Session
from src.model.dataentry import Hospital
from src.schema.findings import UpdateVisitInfoRequest

def update_visit_info(db: Session, data: UpdateVisitInfoRequest):
    hospital = db.query(Hospital).filter(Hospital.id == data.hospital_id).first()
    if not hospital:
        return None

    if data.visit_status is not None:
        hospital.visit_status = data.visit_status
    if data.visit_remark is not None:
        hospital.visit_remark = data.visit_remark

    db.commit()
    db.refresh(hospital)

    return {
        "hospital_id": hospital.id,
        "visit_status": hospital.visit_status,
        "visit_remark": hospital.visit_remark
    }
