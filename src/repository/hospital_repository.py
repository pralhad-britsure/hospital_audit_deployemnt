from sqlalchemy.orm import Session
from src.model.dataentry import Hospital

def get_full_hospital_data_by_id(db: Session, hospital_id: int):
    return db.query(Hospital).filter(Hospital.id == hospital_id).first()
