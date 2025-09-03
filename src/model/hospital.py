from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class BasicInfo(Base):
    __tablename__ = "basic_info"

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey("hospital.id"))
    hospital_name = Column(String(255))
    address = Column(Text)
    location_city = Column(String(100))
    state = Column(String(50))
    area_type = Column(String(30))
    hospital_ownership_type = Column(String(30))
    run_by = Column(String(255))
    owned_by = Column(String(255))
    qualification_of_owner = Column(String(50))
    hospital_type = Column(String(30))
    specialty_type = Column(String(50))
    specialty = Column(Text)
    specialty_other = Column(Text)
    rohini_id = Column(String(100))
    unique_code = Column(String(20))
    audit_status = Column(String(50))

    hospital = relationship("Hospital", back_populates="basic_info")



class RegistrationDetails(Base):
    __tablename__ = 'registration_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    hospital_registration_number = Column(String(100))
    registered_with = Column(String(255))
    registration_valid_up_to = Column(Date)
    registration_number_of_beds = Column(Integer)
    mtp_registration = Column(String(100))
    pndt_registration = Column(String(100))
    organ_transplant_registration = Column(String(100))
    state_clinical_license = Column(String(100))
    nabh_accreditation = Column(String(20))
    nabl_accreditation = Column(String(20))
    jci_accreditation = Column(String(20))
    iso_certification = Column(String(100))
    bio_medical_waste_mgmt_registration = Column(String(100))
    fire_safety_registration = Column(String(255))
    other_certifications = Column(Text)
    gst_number = Column(String(50))
    tan_number = Column(String(50))
    pan_number = Column(String(50))
    pan_name = Column(String(255))
    establishment_year = Column(Integer)
    certificate_of_incorporation = Column(Text)
    document_consistency_verified = Column(Boolean)
    edited_certificates_found = Column(Boolean)
    audit_status = Column(String(50))

    hospital = relationship("Hospital", back_populates="registration_details")


class EmpanelmentDetails(Base):
    __tablename__ = 'empanelment_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    govt_schemes_run = Column(Text)
    govt_schemes_run_other = Column(Text)
    tpas_empaneled = Column(Text)
    tpas_empaneled_other = Column(Text)
    insurance_companies_empaneled = Column(Text)
    corporates_empaneled = Column(Text)
    audit_status = Column(String(50))

    hospital = relationship("Hospital", back_populates="empanelment_details")

class StaffDetails(Base):
    __tablename__ = 'staff_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    medical_superintendent_name = Column(String(255))
    medical_superintendent_working_type = Column(String(20))
    medical_superintendent_contact = Column(String(15))
    medical_director_name = Column(String(255))
    medical_director_working_type = Column(String(20))
    medical_director_contact = Column(String(15))
    hospital_manager_name = Column(String(255))
    hospital_manager_working_type = Column(String(20))
    hospital_manager_contact = Column(String(15))
    tpa_insurance_incharge_name = Column(String(255))
    tpa_insurance_incharge_working_type = Column(String(20))
    tpa_insurance_incharge_contact = Column(String(15))
    nursing_incharge_name = Column(String(255))
    nursing_incharge_working_type = Column(String(20))
    nursing_incharge_contact = Column(String(15))
    surgeon_name = Column(String(255))
    surgeon_working_type = Column(String(20))
    surgeon_contact = Column(String(15))
    physician_name = Column(String(255))
    physician_working_type = Column(String(20))
    physician_contact = Column(String(15))
    intensivist_name = Column(String(255))
    intensivist_working_type = Column(String(20))
    intensivist_contact = Column(String(15))
    pathologist_name = Column(String(255))
    pathologist_working_type = Column(String(20))
    pathologist_contact = Column(String(15))
    lab_technician_name = Column(String(255))
    lab_technician_working_type = Column(String(20))
    lab_technician_contact = Column(String(15))
    radiologist_name = Column(String(255))
    radiologist_working_type = Column(String(20))
    radiologist_contact = Column(String(15))
    key_doctor_registration_numbers = Column(Text)
    clinician_sample_registrations = Column(Text)
    nurse_sample_registrations = Column(Text)
    number_of_specialist_doctors = Column(Integer)
    number_of_super_specialist_doctors = Column(Integer)
    number_of_mbbs_and_above_doctors = Column(Integer)
    number_of_trained_nurses = Column(Integer)
    number_of_housemen = Column(Integer)
    number_of_resident_doctors = Column(Integer)
    number_of_untrained_nurses = Column(Integer)
    number_of_admin_staff = Column(Integer)
    number_of_other_staff = Column(Integer)
    total_number_of_staff = Column(Integer)
    nurse_to_patient_ratio = Column(String(10))
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="staff_details")


class InfrastructureDetails(Base):
    __tablename__ = 'infrastructure_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    type_of_building = Column(String(30))
    area_in_square_feet = Column(Integer)
    number_of_floors = Column(Integer)
    number_of_beds = Column(Integer)
    licensed_bed_count = Column(Integer)
    in_house_lab = Column(Boolean)
    in_house_pharmacy = Column(Boolean)
    ambulance_service = Column(Boolean)
    reception = Column(Boolean)
    tpa_insurance_department = Column(Boolean)
    patient_counselling_area = Column(Boolean)
    physiotherapy_department = Column(Boolean)
    admin_office_present = Column(Boolean)
    number_of_opds = Column(Integer)
    number_of_icus = Column(Integer)
    total_icu_beds = Column(Integer)
    special_rooms = Column(Integer)
    semi_special_rooms = Column(Integer)
    number_of_suites = Column(Integer)
    number_of_general_wards = Column(Integer)
    number_of_general_ward_beds = Column(Integer)
    types_of_operation_theaters = Column(Text)
    number_of_operation_theaters = Column(Integer)
    central_oxygen_supply = Column(Boolean)
    number_of_ventilators = Column(Integer)
    infra_equipment_validation = Column(Text)
    infrastructure_verified = Column(Boolean)
    other_infrastructure = Column(Text)
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="infrastructure_details")

class LabDetails(Base):
    __tablename__ = 'lab_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    lab_name = Column(String(255))
    lab_pathologist_name = Column(String(255))
    lab_pathologist_type = Column(String(30))
    qualification_of_lab_pathologist = Column(String(50))
    pathologist_own_lab_name_location = Column(String(255))
    lab_equipment_available = Column(Boolean)
    type_of_tests_done = Column(Text)
    tests_outsourced = Column(Text)
    xray_machine = Column(Boolean)
    c_arm_machine = Column(Boolean)
    ct_scan = Column(Boolean)
    mri_machine = Column(Boolean)
    usg_machine = Column(Boolean)
    other_diagnostic_equipment = Column(Text)
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="lab_details")

class PharmacyDetails(Base):
    __tablename__ = 'pharmacy_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    pharmacy_name = Column(String(255))
    pharmacy_drug_license_number = Column(String(255))
    pharmacy_working_hours = Column(String(100))
    pharmacist_name = Column(String(255))
    pharmacist_registration_number = Column(String(255))
    stock_register = Column(Boolean)
    purchase_bills = Column(Boolean)
    sales_register = Column(Boolean)
    other_pharmacy_documentation = Column(Text)
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="pharmacy_details")

class RegistersProtocols(Base):
    __tablename__ = 'registers_protocols'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    ipd_register = Column(Boolean)
    icu_register = Column(Boolean)
    opd_register = Column(Boolean)
    operation_theater_register = Column(Boolean)
    lab_register = Column(Boolean)
    mlc_register = Column(Boolean)
    infection_control_protocols = Column(Boolean)
    consultant_visits_register = Column(Boolean)
    salary_slips_available = Column(Boolean)
    salary_payment_mode = Column(Boolean)
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="registers_protocols")

class FinancialDetails(Base):
    __tablename__ = 'financial_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    bank_account_number = Column(String(100))
    ifsc_code = Column(String(20))
    cancelled_cheque_copy = Column(String(255))
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="financial_details")

class BagicDetails(Base):
    __tablename__ = 'bagic_details'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    bagic_to_other_patients_ratio = Column(String(50))
    average_stay = Column(Integer)
    surgical_to_medical_packages_ratio = Column(String(50))
    bagic_mou_copy = Column(String(10))
    bagic_soc_type = Column(String(20))
    bagic_empanelment_done_by = Column(String(30))
    bagic_empanelment_experience = Column(String(20))
    bagic_claim_approval_experience = Column(String(20))
    bagic_claim_verification_experience = Column(String(20))
    bagic_payments_experience = Column(String(20))
    suggestion_for_bagic = Column(Text)
    audit_status = Column(String(50))
    hospital = relationship("Hospital", back_populates="bagic_details")

# class DigitalEvidence(Base):
#     __tablename__ = 'digital_evidence'
#
#     id = Column(Integer, primary_key=True)
#     hospital_id = Column(Integer, ForeignKey('hospital.id'))
#     hospital_photographs = Column(Text)
#     hospital_stamp_photo = Column(String(255))
#     auditor_signature = Column(String(255))
#     hospital_representative_signature = Column(String(255))
#     website_url = Column(String(255))
#     website_valid = Column(Boolean)
#     suspicious_google_reviews_found = Column(Boolean)
#     photo_originality_verified = Column(Boolean)
#     audit_status = Column(String(50))
#     #hospital = relationship("Hospital", back_populates="digital")

class AuditMetadata(Base):
    __tablename__ = 'audit_metadata'

    id = Column(Integer, primary_key=True)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    date_of_visit = Column(Date)
    visit_done_by = Column(String(255))
    attended_by = Column(String(255))
    designation = Column(Text)
    information_given_by = Column(String(255))
    remark_by_auditor = Column(String(255))
    remark_by_hospital_manager_owner = Column(String(255))
    hospital_manager_owner_name = Column(String(255))
    new_setup_claim_verified = Column(Boolean)
    human_presence_verified = Column(Boolean)
    local_market_intel_remarks = Column(Text)
    repeat_tpa_fraud_suspected = Column(Boolean)
    audit_status = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    hospital = relationship("Hospital", back_populates="audit_metadata")
