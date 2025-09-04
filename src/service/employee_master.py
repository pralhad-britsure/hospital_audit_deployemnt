from sqlalchemy.orm import Session
from src.model.user import Employee, user_access_association, AccessType
from src.schema.employee_master import  EmployeeUpdate
from typing import Dict, Any, Optional
from passlib.context import CryptContext
from src.schema.employee_master import EmployeeResponse
from sqlalchemy import or_

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.EmployeeID == employee_id).first()


def get_all_employees(db: Session, search: Optional[str] = None, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
    query = db.query(Employee)

    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            or_(
                Employee.username.ilike(search_pattern),
                Employee.EmployeeName.ilike(search_pattern),
                Employee.MobileNo.ilike(search_pattern),
                Employee.PhoneNo.ilike(search_pattern),
                Employee.State.ilike(search_pattern),
                Employee.District.ilike(search_pattern),
                Employee.Taluka.ilike(search_pattern),
                Employee.City.ilike(search_pattern),
                Employee.Pin.ilike(search_pattern),
                Employee.Area.ilike(search_pattern),
                Employee.EmailAddress.ilike(search_pattern),
                Employee.Designation.ilike(search_pattern),
            )
        )

    # Pagination
    total_records = query.count()
    total_pages = (total_records + page_size - 1) // page_size  # ceil division
    employees = query.offset((page - 1) * page_size).limit(page_size).all()

    return {
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "total_records": total_records,
        "employees": [EmployeeResponse.from_orm(emp) for emp in employees]
    }


def update_employee(db: Session, employee_id: int, emp: EmployeeUpdate):
    db_emp = db.query(Employee).filter(Employee.EmployeeID == employee_id).first()
    if not db_emp:
        return None
    for key, value in emp.dict(exclude_unset=True).items():
        setattr(db_emp, key, value)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def toggle_employee_status(db: Session, employee_id: int):
    db_emp = db.query(Employee).filter(Employee.EmployeeID == employee_id).first()
    if not db_emp:
        return None

    # Toggle status
    db_emp.is_active = not db_emp.is_active
    db.commit()
    db.refresh(db_emp)
    return db_emp
