# from sqlalchemy.orm import Session
# from src.model.dataentry import Hospital
#
# def mark_hospital_completed(db: Session, hospital_id: int):
#     hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
#     if not hospital:
#         return None
#     hospital.audit_status = "completed"
#     db.commit()
#     db.refresh(hospital)
#     return hospital
#
# def reallocate_hospital(db: Session, hospital_id: int):
#     hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
#     if not hospital:
#         return None
#     hospital.fo = None
#     hospital.visit_status = None
#     hospital.visit_remark = None
#     hospital.status = "allocation"
#     db.commit()
#     db.refresh(hospital)
#     return hospital


from sqlalchemy.orm import Session
from src.model.dataentry import Hospital


def mark_hospital_completed(db: Session, hospital_id: int):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        return None
    hospital.audit_status = "completed"
    db.commit()
    db.refresh(hospital)
    return {"id": hospital.id, "status": "Completed"}


def reallocate_hospital(db: Session, hospital_id: int):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        return None
    hospital.fo = None
    hospital.visit_status = None
    hospital.visit_remark = None
    hospital.status = "allocation"
    db.commit()
    db.refresh(hospital)

    # Custom response
    return {"id": hospital.id, "status": "Reallocation available"}
