from sqlalchemy.orm import Session
from src.model.dataentry import Hospital
from src.schema.dataentry import HospitalCreate, HospitalBulkEntryCreate

def create_hospital(db: Session, hospital: HospitalCreate):
    db_hospital = Hospital(
        hospital_name=hospital.hospital_name,
        address=hospital.address,
        location_city=hospital.location_city,
        state=hospital.state,
        Dist=hospital.Dist,
        Taluka=hospital.Taluka,
        senior_manager=hospital.senior_manager,
        executive=hospital.executive,
        data_entry_operator=hospital.data_entry_operator,
        status="allocation"
    )
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital


def bulk_create_hospitals(db: Session, hospitals: list[HospitalBulkEntryCreate], senior_manager: int, executive: int, data_entry_operator: int):
    db_objs = [
        Hospital(
            hospital_name=h.hospital_name,
            address=h.address,
            location_city=h.location_city,
            state=h.state,
            Dist=h.Dist,
            Taluka=h.Taluka,
            senior_manager=senior_manager,
            executive=executive,
            data_entry_operator=data_entry_operator,
            status="allocation"

        )
        for h in hospitals
    ]
    db.add_all(db_objs)
    db.commit()
    return {"message": f"{len(db_objs)} hospitals created with senior_manager={senior_manager} and executive={executive}"}
