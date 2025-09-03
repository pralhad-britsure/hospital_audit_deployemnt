from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from src.database import get_db
from src.schema.employee_master import EmployeeResponse, EmployeeUpdate
from src.service import employee_master

router = APIRouter(prefix="/hospital", tags=["Employees Master"])


@router.get("/", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return employee_master.get_all_employees(db)


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


@router.put("/{employee_id}/deactivate", response_model=Dict[str, Any])
def deactivate_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = employee_master.deactivate_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "message": "Employee deactivated successfully",
        # "employee": EmployeeResponse.model_validate(emp)
    }