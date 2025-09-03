from sqlalchemy.orm import Session
from src.model.user import Employee, user_access_association, AccessType
from src.schema.employee_master import  EmployeeUpdate
from typing import List
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.EmployeeID == employee_id).first()


def get_all_employees(db: Session) -> List[Employee]:
    return db.query(Employee).all()



def update_employee(db: Session, employee_id: int, emp: EmployeeUpdate):
    db_emp = db.query(Employee).filter(Employee.EmployeeID == employee_id).first()
    if not db_emp:
        return None
    for key, value in emp.dict(exclude_unset=True).items():
        setattr(db_emp, key, value)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def deactivate_employee(db: Session, employee_id: int):
    db_emp = db.query(Employee).filter(Employee.EmployeeID == employee_id).first()
    if not db_emp:
        return None
    db_emp.is_active = False
    db.commit()
    return db_emp
