# from sqlalchemy import Column, Integer, String, Text, Enum, Date, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Date, Text, TIMESTAMP, func
# from src.enum import (
#     StateEnum, AreaTypeEnum, OwnershipTypeEnum, QualificationEnum,
#     HospitalTypeEnum, SpecialtyTypeEnum, YesNoAppliedEnum, WorkingTypeEnum, BuildingOwnershipEnum, BuildingTypeEnum,
#     LabPathologistTypeEnum, LabPathologistQualificationEnum, YesNoEnum, BagicEmpanelmentByEnum, BagicSocTypeEnum,
#     ExperienceRatingEnum
# )
#
# Base = declarative_base()
#
# class HospitalAudit(Base):
#     __tablename__ = 'hospital_audit'
#
#     hosp_id = Column(Integer, primary_key=True, autoincrement=True)
#     hospital_name = Column(String(255))
#     address = Column(Text)
#     location_city = Column(String(100))
#     state = Column(Enum(StateEnum))
#     area_type = Column(Enum(AreaTypeEnum))
#     hospital_ownership_type = Column(Enum(OwnershipTypeEnum))
#     run_by = Column(String(255))
#     owned_by = Column(String(255))
#     qualification_of_owner = Column(Enum(QualificationEnum))
#     hospital_type = Column(Enum(HospitalTypeEnum))
#     specialty_type = Column(Enum(SpecialtyTypeEnum))
#     specialty = Column(Text)
#     specialty_other = Column(Text)
#     govt_schemes_run = Column(Text)
#     govt_schemes_run_other = Column(Text)
#     tpas_empaneled = Column(Text)
#     tpas_empaneled_other = Column(Text)
#     insurance_companies_empaneled = Column(Text)
#     corporates_empaneled = Column(Text)
#
#     hospital_registration_number = Column(String(100))
#     registered_with = Column(String(255))
#     registration_valid_up_to = Column(Date)
#     registration_number_of_beds = Column(Integer)
#     mtp_registration = Column(String(100))
#     pndt_registration = Column(String(100))
#     organ_transplant_registration = Column(String(100))
#     nabh_accreditation = Column(Enum(YesNoAppliedEnum))
#     bio_medical_waste_mgmt_registration = Column(String(100))
#     iso_certification = Column(String(100))
#     other_certifications = Column(Text)
#     cctv_system = Column(Boolean)
#     security_arrangement = Column(Boolean)
#     fire_safety_registration = Column(String(255))
#     staff_health_insurance_policies = Column(String(255))
#     staff_group_mediclaim_insurer = Column(String(255))
#     other_compliance_documents = Column(Text)
#
#     medical_superintendent_name = Column(String(255))
#     medical_superintendent_working_type = Column(Enum(WorkingTypeEnum))
#     medical_superintendent_contact = Column(String(15))
#
#     medical_director_name = Column(String(255))
#     medical_director_working_type = Column(Enum(WorkingTypeEnum))
#     medical_director_contact = Column(String(15))
#
#     hospital_manager_name = Column(String(255))
#     hospital_manager_working_type = Column(Enum(WorkingTypeEnum))
#     hospital_manager_contact = Column(String(15))
#
#     tpa_insurance_incharge_name = Column(String(255))
#     tpa_insurance_incharge_working_type = Column(Enum(WorkingTypeEnum))
#     tpa_insurance_incharge_contact = Column(String(15))
#
#     nursing_incharge_name = Column(String(255))
#     nursing_incharge_working_type = Column(Enum(WorkingTypeEnum))
#     nursing_incharge_contact = Column(String(15))
#
#     surgeon_name = Column(String(255))
#     surgeon_working_type = Column(Enum(WorkingTypeEnum))
#     surgeon_contact = Column(String(15))
#
#     physician_name = Column(String(255))
#     physician_working_type = Column(Enum(WorkingTypeEnum))
#     physician_contact = Column(String(15))
#
#     intensivist_name = Column(String(255))
#     intensivist_working_type = Column(Enum(WorkingTypeEnum))
#     intensivist_contact = Column(String(15))
#
#     pathologist_name = Column(String(255))
#     pathologist_working_type = Column(Enum(WorkingTypeEnum))
#     pathologist_contact = Column(String(15))
#
#     lab_technician_name = Column(String(255))
#     lab_technician_working_type = Column(Enum(WorkingTypeEnum))
#     lab_technician_contact = Column(String(15))
#
#     radiologist_name = Column(String(255))
#     radiologist_working_type = Column(Enum(WorkingTypeEnum))
#     radiologist_contact = Column(String(15))
#
#     number_of_specialist_doctors = Column(Integer, default=0)
#     number_of_super_specialist_doctors = Column(Integer, default=0)
#     number_of_mbbs_and_above_doctors = Column(Integer, default=0)
#     number_of_trained_nurses = Column(Integer, default=0)
#     number_of_housemen = Column(Integer, default=0)
#     number_of_resident_doctors = Column(Integer, default=0)
#     number_of_untrained_nurses = Column(Integer, default=0)
#     number_of_admin_staff = Column(Integer, default=0)
#     number_of_other_staff = Column(Integer, default=0)
#     total_number_of_staff = Column(Integer, default=0)
#
#     type_of_building = Column(Enum(BuildingTypeEnum))
#     number_of_beds = Column(Integer)
#     in_house_lab = Column(Boolean)
#     in_house_pharmacy = Column(Boolean)
#     number_of_opds = Column(Integer, default=0)
#     number_of_icus = Column(Integer, default=0)
#     total_icu_beds = Column(Integer, default=0)
#     special_rooms = Column(Integer, default=0)
#     semi_special_rooms = Column(Integer, default=0)
#     number_of_suites = Column(Integer, default=0)
#     number_of_general_wards = Column(Integer, default=0)
#     number_of_general_ward_beds = Column(Integer, default=0)
#     types_of_operation_theaters = Column(Text)
#     number_of_operation_theaters = Column(Integer, default=0)
#     central_oxygen_supply = Column(Boolean)
#     number_of_ventilators = Column(Integer, default=0)
#     area_in_square_feet = Column(Integer)
#     number_of_floors = Column(Integer)
#     building_ownership = Column(Enum(BuildingOwnershipEnum))
#     ambulance_service = Column(Boolean)
#     reception = Column(Boolean)
#     tpa_insurance_department = Column(Boolean)
#     patient_counselling_area = Column(Boolean)
#     physiotherapy_department = Column(Boolean)
#     other_infrastructure = Column(Text)
#
#     # Lab section
#     lab_name = Column(String(255))
#     lab_pathologist_name = Column(String(255))
#     lab_pathologist_type = Column(Enum(LabPathologistTypeEnum))
#     qualification_of_lab_pathologist = Column(Enum(LabPathologistQualificationEnum))
#     pathologist_own_lab_name_location = Column(String(255))
#     lab_equipment_available = Column(Boolean)
#     type_of_tests_done = Column(Text)
#     tests_outsourced = Column(Text)
#     xray_machine = Column(Boolean)
#     c_arm_machine = Column(Boolean)
#     ct_scan = Column(Boolean)
#     mri_machine = Column(Boolean)
#     usg_machine = Column(Boolean)
#     other_diagnostic_equipment = Column(Text)
#
#     # Pharmacy section
#     pharmacy_name = Column(String(255))
#     pharmacy_drug_license_number = Column(String(255))
#     pharmacy_working_hours = Column(String(100))
#     pharmacist_name = Column(String(255))
#     pharmacist_registration_number = Column(String(255))
#     stock_register = Column(Boolean)
#     purchase_bills = Column(Boolean)
#     sales_register = Column(Boolean)
#     other_pharmacy_documentation = Column(Text)
#
#     ipd_register = Column(Boolean)
#     icu_register = Column(Boolean)
#     opd_register = Column(Boolean)
#     operation_theater_register = Column(Boolean)
#     lab_register = Column(Boolean)
#     mlc_register = Column(Boolean)
#     infection_control_protocols = Column(Boolean)
#     consultant_visits_register = Column(Boolean)
#     salary_slips_available = Column(Boolean)
#     salary_payment_mode = Column(Boolean)
#
#     # BAGIC Section
#     bagic_to_other_patients_ratio = Column(String(50))
#     average_stay = Column(Integer)
#     surgical_to_medical_packages_ratio = Column(String(50))
#     bagic_mou_copy = Column(Enum(YesNoEnum))
#     bagic_soc_type = Column(Enum(BagicSocTypeEnum))
#     bagic_empanelment_done_by = Column(Enum(BagicEmpanelmentByEnum))
#     bagic_empanelment_experience = Column(Enum(ExperienceRatingEnum))
#     bagic_claim_approval_experience = Column(Enum(ExperienceRatingEnum))
#     bagic_claim_verification_experience = Column(Enum(ExperienceRatingEnum))
#     bagic_payments_experience = Column(Enum(ExperienceRatingEnum))
#     suggestion_for_bagic = Column(Text)
#
#     # Audit Completion
#     date_of_visit = Column(Date)
#     visit_done_by = Column(String(255))
#     attended_by = Column(String(255))
#     designation = Column(Text)
#     information_given_by = Column(String(255))
#     remark_by_auditor = Column(String(255))
#     remark_by_hospital_manager_owner = Column(String(255))
#     auditor_signature = Column(String(255))
#     hospital_manager_owner_name = Column(String(255))
#     hospital_representative_signature = Column(String(255))
#     hospital_stamp_photo = Column(String(255))
#
#     # Audit Metadata
#     created_at = Column(TIMESTAMP, server_default=func.now())
#     updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


from sqlalchemy import Column, Integer, String, Text, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import TIMESTAMP, func

Base = declarative_base()


class HospitalAudit(Base):
    __tablename__ = 'hospital_audit'

    hosp_id = Column(Integer, primary_key=True, autoincrement=True)
    hospital_name = Column(String(255))
    address = Column(Text)
    location_city = Column(String(100))

    # Changed from Enum to String to avoid truncation issues
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
    govt_schemes_run = Column(Text)
    govt_schemes_run_other = Column(Text)
    tpas_empaneled = Column(Text)
    tpas_empaneled_other = Column(Text)
    insurance_companies_empaneled = Column(Text)
    corporates_empaneled = Column(Text)

    hospital_registration_number = Column(String(100))
    registered_with = Column(String(255))
    registration_valid_up_to = Column(Date)
    registration_number_of_beds = Column(Integer)
    mtp_registration = Column(String(100))
    pndt_registration = Column(String(100))
    organ_transplant_registration = Column(String(100))
    nabh_accreditation = Column(String(20))  # Changed from Enum
    bio_medical_waste_mgmt_registration = Column(String(100))
    iso_certification = Column(String(100))
    other_certifications = Column(Text)
    cctv_system = Column(Boolean)
    security_arrangement = Column(Boolean)
    fire_safety_registration = Column(String(255))
    staff_health_insurance_policies = Column(String(255))
    staff_group_mediclaim_insurer = Column(String(255))
    other_compliance_documents = Column(Text)

    medical_superintendent_name = Column(String(255))
    medical_superintendent_working_type = Column(String(20))  # Changed from Enum
    medical_superintendent_contact = Column(String(15))

    medical_director_name = Column(String(255))
    medical_director_working_type = Column(String(20))  # Changed from Enum
    medical_director_contact = Column(String(15))

    hospital_manager_name = Column(String(255))
    hospital_manager_working_type = Column(String(20))  # Changed from Enum
    hospital_manager_contact = Column(String(15))

    tpa_insurance_incharge_name = Column(String(255))
    tpa_insurance_incharge_working_type = Column(String(20))  # Changed from Enum
    tpa_insurance_incharge_contact = Column(String(15))

    nursing_incharge_name = Column(String(255))
    nursing_incharge_working_type = Column(String(20))  # Changed from Enum
    nursing_incharge_contact = Column(String(15))

    surgeon_name = Column(String(255))
    surgeon_working_type = Column(String(20))  # Changed from Enum
    surgeon_contact = Column(String(15))

    physician_name = Column(String(255))
    physician_working_type = Column(String(20))  # Changed from Enum
    physician_contact = Column(String(15))

    intensivist_name = Column(String(255))
    intensivist_working_type = Column(String(20))  # Changed from Enum
    intensivist_contact = Column(String(15))

    pathologist_name = Column(String(255))
    pathologist_working_type = Column(String(20))  # Changed from Enum
    pathologist_contact = Column(String(15))

    lab_technician_name = Column(String(255))
    lab_technician_working_type = Column(String(20))  # Changed from Enum
    lab_technician_contact = Column(String(15))

    radiologist_name = Column(String(255))
    radiologist_working_type = Column(String(20))  # Changed from Enum
    radiologist_contact = Column(String(15))

    number_of_specialist_doctors = Column(Integer, default=0)
    number_of_super_specialist_doctors = Column(Integer, default=0)
    number_of_mbbs_and_above_doctors = Column(Integer, default=0)
    number_of_trained_nurses = Column(Integer, default=0)
    number_of_housemen = Column(Integer, default=0)
    number_of_resident_doctors = Column(Integer, default=0)
    number_of_untrained_nurses = Column(Integer, default=0)
    number_of_admin_staff = Column(Integer, default=0)
    number_of_other_staff = Column(Integer, default=0)
    total_number_of_staff = Column(Integer, default=0)

    type_of_building = Column(String(30))  # Changed from Enum
    number_of_beds = Column(Integer)
    in_house_lab = Column(Boolean)
    in_house_pharmacy = Column(Boolean)
    number_of_opds = Column(Integer, default=0)
    number_of_icus = Column(Integer, default=0)
    total_icu_beds = Column(Integer, default=0)
    special_rooms = Column(Integer, default=0)
    semi_special_rooms = Column(Integer, default=0)
    number_of_suites = Column(Integer, default=0)
    number_of_general_wards = Column(Integer, default=0)
    number_of_general_ward_beds = Column(Integer, default=0)
    types_of_operation_theaters = Column(Text)
    number_of_operation_theaters = Column(Integer, default=0)
    central_oxygen_supply = Column(Boolean)
    number_of_ventilators = Column(Integer, default=0)
    area_in_square_feet = Column(Integer)
    number_of_floors = Column(Integer)
    building_ownership = Column(String(30))  # Changed from Enum
    ambulance_service = Column(Boolean)
    reception = Column(Boolean)
    tpa_insurance_department = Column(Boolean)
    patient_counselling_area = Column(Boolean)
    physiotherapy_department = Column(Boolean)
    other_infrastructure = Column(Text)

    # Lab section
    lab_name = Column(String(255))
    lab_pathologist_name = Column(String(255))
    lab_pathologist_type = Column(String(30))  # Changed from Enum
    qualification_of_lab_pathologist = Column(String(50))  # Changed from Enum
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

    # Pharmacy section
    pharmacy_name = Column(String(255))
    pharmacy_drug_license_number = Column(String(255))
    pharmacy_working_hours = Column(String(100))
    pharmacist_name = Column(String(255))
    pharmacist_registration_number = Column(String(255))
    stock_register = Column(Boolean)
    purchase_bills = Column(Boolean)
    sales_register = Column(Boolean)
    other_pharmacy_documentation = Column(Text)

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

    # BAGIC Section
    bagic_to_other_patients_ratio = Column(String(50))
    average_stay = Column(Integer)
    surgical_to_medical_packages_ratio = Column(String(50))
    bagic_mou_copy = Column(String(10))  # Changed from Enum
    bagic_soc_type = Column(String(20))  # Changed from Enum
    bagic_empanelment_done_by = Column(String(30))  # Changed from Enum
    bagic_empanelment_experience = Column(String(20))  # Changed from Enum
    bagic_claim_approval_experience = Column(String(20))  # Changed from Enum
    bagic_claim_verification_experience = Column(String(20))  # Changed from Enum
    bagic_payments_experience = Column(String(20))  # Changed from Enum
    suggestion_for_bagic = Column(Text)

    # Audit Completion
    date_of_visit = Column(Date)
    visit_done_by = Column(String(255))
    attended_by = Column(String(255))
    designation = Column(Text)
    information_given_by = Column(String(255))
    remark_by_auditor = Column(String(255))
    remark_by_hospital_manager_owner = Column(String(255))
    auditor_signature = Column(String(255))
    hospital_manager_owner_name = Column(String(255))
    hospital_representative_signature = Column(String(255))
    hospital_stamp_photo = Column(String(255))

    # Audit Metadata
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    unique_code = Column(String(20))
