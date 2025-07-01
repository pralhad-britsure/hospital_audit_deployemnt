import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.auth import router as auth_router
from src.api.hospital_audit import router as hospital_audit_router
from src.api.sftp_upload import router as sftp_upload_router
from src.api.random import router as random_router
from src.models.user import Base
from src.database import engine

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
app.include_router(hospital_audit_router)
app.include_router(sftp_upload_router)
app.include_router(random_router)


@app.get("/")
def read_root():
    return {"message": "Welcome Hospital Audit API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
