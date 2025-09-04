from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session
from typing import List, Dict, Any,Optional
from src.database import get_db
from src.schema.employee_master import EmployeeResponse, EmployeeUpdate
from src.service import employee_master

router = APIRouter(prefix="/hospital", tags=["Employees Master"])


@router.get("/", response_model=Dict[str, Any])
def get_employees(
    db: Session = Depends(get_db),
    search: Optional[str] = Query(None, description="Search employees by name, username, mobile, etc."),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Records per page")
):
    return employee_master.get_all_employees(db, search=search, page=page, page_size=page_size)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = employee_master.get_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{employee_id}", response_model=Dict[str, Any])
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    emp = employee_master.update_employee(db, employee_id, employee)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "message": "Employee updated successfully",
        # "employee": EmployeeResponse.model_validate(emp)
    }

@router.put("/{employee_id}/toggle", response_model=Dict[str, Any])
def toggle_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = employee_master.toggle_employee_status(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    status = "activated" if emp.is_active else "deactivated"

    return {
        "message": f"Employee {status} successfully",
        # "employee": EmployeeResponse.from_orm(emp)
    }