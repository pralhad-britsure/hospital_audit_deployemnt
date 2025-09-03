from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.model.user import Employee
from src.schema.send_email import EmailRequest
from src.utils.email import send_email

router = APIRouter(prefix="/email", tags=["Email"])

@router.post("/send-allocation-email")
def send_allocation_email(payload: EmailRequest, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.EmployeeID == payload.employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    body = (
        f"Dear {employee.EmployeeName},\n\n"
       
        f"You have been assigned a new hospital for Infrastructure Audit "
        f"Please find the details below:\n\n"
        f"Hospital Name : {payload.hospital_name}\n"
        f"Address       : {payload.address}\n"
        f"City          : {payload.city}\n"
        f"Taluka        : {payload.taluka}\n"
        f"District      : {payload.district}\n\n"
         
        f"If you have any questions or require further assistance, please do not hesitate to contact the audit coordination team.\n\n"
        
        f"Best regards,\n"
        f"Senior Manager\n"
        f"Wasim Khan\n"
        f"Contact - 8956103001"
)

    subject = "New Case Allocation"

    sent = send_email(subject, employee.EmailAddress, body)

    if sent:
        return {"message": f"Email sent successfully to {employee.EmailAddress}"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send email")
