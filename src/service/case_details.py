from sqlalchemy.orm import Session, aliased
from sqlalchemy import or_, and_, func
from datetime import date
from src.model.dataentry import Hospital
#
# def get_filtered_hospitals(
#     db: Session,
#     employee_id: int = None,
#     from_date: date = None,
#     to_date: date = None,
#     received_date: date = None,
#     search: str = None
# ):
#     query = db.query(Hospital)
#
#     # Filter by employee_id
#     if employee_id:
#         query = query.filter(or_(
#             Hospital.senior_manager == employee_id,
#             Hospital.executive == employee_id,
#             Hospital.fo == employee_id
#         ))
#
#     # Daily received_date filter (default today)
#     if received_date:
#         query = query.filter(func.date(Hospital.received_date) == received_date)
#
#     # Range filter overrides received_date if both present
#     if from_date and to_date:
#         query = query.filter(func.date(Hospital.received_date).between(from_date, to_date))
#
#     # Search filter on text fields
#     if search:
#         search = f"%{search.lower()}%"
#         query = query.filter(or_(
#             func.lower(Hospital.hospital_name).like(search),
#             func.lower(Hospital.address).like(search),
#             func.lower(Hospital.location_city).like(search),
#             func.lower(Hospital.state).like(search),
#             func.lower(Hospital.visit_status).like(search),
#             func.lower(Hospital.visit_remark).like(search),
#             func.lower(Hospital.audit_status).like(search),
#             func.lower(Hospital.status).like(search),
#             func.lower(Hospital.Dist).like(search),
#             func.lower(Hospital.Taluka).like(search)
#         ))
#
#     return query.all()

from src.model.user import Employee

def get_filtered_hospitals(
    db: Session,
    employee_id: int = None,
    from_date: date = None,
    to_date: date = None,
    received_date: date = None,
    search: str = None
):
    emp_alias_sm = aliased(Employee)
    emp_alias_ex = aliased(Employee)
    emp_alias_fo = aliased(Employee)

    query = db.query(
        Hospital,
        emp_alias_sm.EmployeeName.label("senior_manager_name"),
        emp_alias_ex.EmployeeName.label("executive_name"),
        emp_alias_fo.EmployeeName.label("fo_name")
    ).outerjoin(emp_alias_sm, Hospital.senior_manager == emp_alias_sm.EmployeeID
    ).outerjoin(emp_alias_ex, Hospital.executive == emp_alias_ex.EmployeeID
    ).outerjoin(emp_alias_fo, Hospital.fo == emp_alias_fo.EmployeeID)

    # Filters
    if employee_id:
        query = query.filter(or_(
            Hospital.senior_manager == employee_id,
            Hospital.executive == employee_id,
            Hospital.fo == employee_id
        ))

    if received_date:
        query = query.filter(func.date(Hospital.received_date) == received_date)

    if from_date and to_date:
        query = query.filter(func.date(Hospital.received_date).between(from_date, to_date))

    if search:
        search = f"%{search.lower()}%"
        query = query.filter(or_(
            func.lower(Hospital.hospital_name).like(search),
            func.lower(Hospital.address).like(search),
            func.lower(Hospital.location_city).like(search),
            func.lower(Hospital.state).like(search),
            func.lower(Hospital.visit_status).like(search),
            func.lower(Hospital.visit_remark).like(search),
            func.lower(Hospital.audit_status).like(search),
            func.lower(Hospital.status).like(search),
            func.lower(Hospital.Dist).like(search),
            func.lower(Hospital.Taluka).like(search)
        ))

    results = query.all()

    response = []
    for hospital, sm_name, ex_name, fo_name in results:
        hospital_dict = hospital.__dict__.copy()
        hospital_dict["senior_manager_name"] = sm_name
        hospital_dict["executive_name"] = ex_name
        hospital_dict["fo_name"] = fo_name
        response.append(hospital_dict)

    return response
