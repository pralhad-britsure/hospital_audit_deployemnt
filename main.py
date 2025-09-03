import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.auth import router as auth_router
from src.api.hospital import router as hospital_basic
from src.model.user import Base
from src.database import engine

from src.api.dataentry import router as data_entry_router
from src.api.case_details import router as case_details_router
from src.api.findings import router as findings_router
from src.api.reports import router as reports_router
from src.api.get_all_reports import router as get_all_routers
from src.api.sftp_upload import router as sftp_router
from src.api.send_email import router as send_email_router
from src.api.employee_master import router as employee_master_router

app = FastAPI(title="Hospital Audit API")
Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix='/auth')
app.include_router(hospital_basic)
app.include_router(data_entry_router)
app.include_router(case_details_router)
app.include_router(findings_router)
app.include_router(reports_router)
app.include_router(get_all_routers)
app.include_router(sftp_router)
app.include_router(send_email_router)
app.include_router(employee_master_router)



@app.get("/")
def read_root():
    return {"message": "Welcome Hospital Audit API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
