from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.model.user import Employee
from src.schema.user import UserCreate
from src.auth.jwt_handler import AuthHandler
from typing import List

auth_handler = AuthHandler()

def create_user(db: Session, user: UserCreate):
    db_user = db.query(Employee).filter(Employee.EmailAddress == user.EmailAddress).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = auth_handler.get_password_hash(user.password)
    db_user = Employee(
        username=user.username,
        EmailAddress=user.EmailAddress,
        hashed_password=hashed_password,
        role=user.role,
        access=user.access,
        EmployeeName=user.EmployeeName,
        MobileNo=user.MobileNo,
        PhoneNo=user.PhoneNo,
        HomeAddress=user.HomeAddress,
        State=user.State,
        District=user.District,
        Taluka=user.Taluka,
        City=user.City,
        Area=user.Area,
        Pin=user.Pin,
        Designation=user.Designation,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(Employee).filter(Employee.EmailAddress == email).first()
    if not user:
        return False
    if not auth_handler.verify_password(password, user.hashed_password):
        return False
    return user

def get_employees_by_role(role: str, db: Session) -> List[Employee]:
    return db.query(Employee).filter(Employee.role == role).all()
