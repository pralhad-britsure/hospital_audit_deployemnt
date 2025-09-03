from fastapi import APIRouter, Depends, HTTPException, status,Query
from sqlalchemy.orm import Session
from typing import List
from src.schema.user import UserCreate, UserResponse, UserLogin, Token, EmployeeSimpleResponse
from src.service.user_service import create_user, authenticate_user, get_employees_by_role
from src.database import get_db
from src.auth.jwt_handler import AuthHandler
from src.model.user import Employee

router = APIRouter(tags=["Authentication"])
auth_handler = AuthHandler()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_credentials.EmailAddress, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_handler.encode_token(user.EmployeeID, user.role)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "access":user.access,
        "EmployeeID": user.EmployeeID
    }

@router.get("/me", response_model=UserResponse)
def get_current_user(auth_data=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    user_id = auth_data["user_id"]
    user = db.query(Employee).filter(Employee.EmployeeID == int(user_id)).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/list-of-employee-by-role", response_model=List[EmployeeSimpleResponse])
def list_employees_by_role(
    role: str = Query(..., description="Role to filter by (e.g., senior_manager, auditor, executive, field_officer)"),
    db: Session = Depends(get_db)
):
    valid_roles = {"senior_manager", "auditor", "executive", "field_officer"}

    if role not in valid_roles:
        raise HTTPException(status_code=400, detail=f"Invalid role: '{role}'. Allowed roles: {', '.join(valid_roles)}")

    employees = get_employees_by_role(role, db)
    return employees


from src.model.dataentry import Hospital
from src.model.user import  Employee
from src.schema.user import HospitalEmployeeResponse
from sqlalchemy.orm import Session, aliased
from typing import Optional, List

@router.get("/hospitals/with-employees", response_model=List[HospitalEmployeeResponse])
def get_hospitals_with_employees(
    fo: Optional[int] = Query(None),
    senior_manager: Optional[int] = Query(None),
    executive: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    # Aliases
    FoEmp = aliased(Employee)
    SeniorEmp = aliased(Employee)
    ExecEmp = aliased(Employee)

    # Start query explicitly from Hospital
    query = db.query(
        Hospital.id.label("hospital_id"),
        Hospital.hospital_name,
        Hospital.address,
        Hospital.location_city,
        Hospital.state,
        FoEmp.EmployeeName.label("fo_name"),
        SeniorEmp.EmployeeName.label("senior_manager_name"),
        ExecEmp.EmployeeName.label("executive_name"),
    ).select_from(Hospital)\
     .outerjoin(FoEmp, Hospital.fo == FoEmp.EmployeeID)\
     .outerjoin(SeniorEmp, Hospital.senior_manager == SeniorEmp.EmployeeID)\
     .outerjoin(ExecEmp, Hospital.executive == ExecEmp.EmployeeID)

    if fo:
        query = query.filter(Hospital.fo == fo)
    if senior_manager:
        query = query.filter(Hospital.senior_manager == senior_manager)
    if executive:
        query = query.filter(Hospital.executive == executive)
    return query.all()



from src.model.user import Employee
from pydantic import BaseModel

class EmployeeNameOut(BaseModel):
    EmployeeName: str

    class Config:
        from_attributes = True

@router.get("/employee-with-filters", response_model=List[EmployeeNameOut])
def filter_employees(
    state: Optional[str] = Query(None),
    district: Optional[str] = Query(None),
    taluka: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Employee)

    if state:
        query = query.filter(Employee.State == state)
    if district:
        query = query.filter(Employee.District == district)
    if taluka:
        query = query.filter(Employee.Taluka == taluka)
    if city:
        query = query.filter(Employee.City == city)

    employees = query.all()
    return employees
