from pydantic import BaseModel ,validator, Field
from typing import Optional, List
from datetime import date, datetime

class BasicInfoBase(BaseModel):
    hospital_id: int
    hospital_name: Optional[str]
    address: Optional[str]
    location_city: Optional[str]
    state: Optional[str]
    area_type: Optional[str]
    hospital_ownership_type: Optional[str]
    run_by: Optional[str]
    owned_by: Optional[str]
    qualification_of_owner: Optional[str]
    hospital_type: Optional[str]
    specialty_type: Optional[str]
    specialty: Optional[str]
    specialty_other: Optional[str]
    rohini_id: Optional[str]
    unique_code: Optional[str]
    audit_status: Optional[str]
    class Config:
        from_attributes = True

class RegistrationCreate(BaseModel):
    hospital_id: Optional[int] = None
    hospital_registration_number: Optional[str] = None
    registered_with: Optional[str] = None
    registration_valid_up_to: Optional[date] = None
    registration_number_of_beds: Optional[int] = None
    mtp_registration: Optional[str] = None
    pndt_registration: Optional[str] = None
    organ_transplant_registration: Optional[str] = None
    state_clinical_license: Optional[str] = None
    nabh_accreditation: Optional[str] = None
    nabl_accreditation: Optional[str] = None
    jci_accreditation: Optional[str] = None
    iso_certification: Optional[str] = None
    bio_medical_waste_mgmt_registration: Optional[str] = None
    fire_safety_registration: Optional[str] = None
    other_certifications: Optional[str] = None
    gst_number: Optional[str] = None
    tan_number: Optional[str] = None
    pan_number: Optional[str] = None
    pan_name: Optional[str] = None
    establishment_year: Optional[int] = None
    certificate_of_incorporation: Optional[str] = None
    document_consistency_verified: Optional[bool] = None
    edited_certificates_found: Optional[bool] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True


    @validator("*", pre=True)
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v

class EmpanelmentCreate(BaseModel):
    hospital_id: Optional[int] = None
    govt_schemes_run: Optional[str] = None
    govt_schemes_run_other: Optional[str] = None
    tpas_empaneled: Optional[str] = None
    tpas_empaneled_other: Optional[str] = None
    insurance_companies_empaneled: Optional[str] = None
    corporates_empaneled: Optional[str] = None
    audit_status: Optional[str] = None
    class Config:
        from_attributes = True


class StaffCreate(BaseModel):
    hospital_id: Optional[int] = None
    medical_superintendent_name: Optional[str] = None
    medical_superintendent_working_type: Optional[str] = None
    medical_superintendent_contact: Optional[str] = None
    medical_director_name: Optional[str] = None
    medical_director_working_type: Optional[str] = None
    medical_director_contact: Optional[str] = None
    hospital_manager_name: Optional[str] = None
    hospital_manager_working_type: Optional[str] = None
    hospital_manager_contact: Optional[str] = None
    tpa_insurance_incharge_name: Optional[str] = None
    tpa_insurance_incharge_working_type: Optional[str] = None
    tpa_insurance_incharge_contact: Optional[str] = None
    nursing_incharge_name: Optional[str] = None
    nursing_incharge_working_type: Optional[str] = None
    nursing_incharge_contact: Optional[str] = None
    surgeon_name: Optional[str] = None
    surgeon_working_type: Optional[str] = None
    surgeon_contact: Optional[str] = None
    physician_name: Optional[str] = None
    physician_working_type: Optional[str] = None
    physician_contact: Optional[str] = None
    intensivist_name: Optional[str] = None
    intensivist_working_type: Optional[str] = None
    intensivist_contact: Optional[str] = None
    pathologist_name: Optional[str] = None
    pathologist_working_type: Optional[str] = None
    pathologist_contact: Optional[str] = None
    lab_technician_name: Optional[str] = None
    lab_technician_working_type: Optional[str] = None
    lab_technician_contact: Optional[str] = None
    radiologist_name: Optional[str] = None
    radiologist_working_type: Optional[str] = None
    radiologist_contact: Optional[str] = None
    key_doctor_registration_numbers: Optional[str] = None
    clinician_sample_registrations: Optional[str] = None
    nurse_sample_registrations: Optional[str] = None
    number_of_specialist_doctors: Optional[int] = None
    number_of_super_specialist_doctors: Optional[int] = None
    number_of_mbbs_and_above_doctors: Optional[int] = None
    number_of_trained_nurses: Optional[int] = None
    number_of_housemen: Optional[int] = None
    number_of_resident_doctors: Optional[int] = None
    number_of_untrained_nurses: Optional[int] = None
    number_of_admin_staff: Optional[int] = None
    number_of_other_staff: Optional[int] = None
    total_number_of_staff: Optional[int] = None
    nurse_to_patient_ratio: Optional[str] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True


class InfrastructureCreate(BaseModel):
    hospital_id: Optional[int] = None
    type_of_building: Optional[str] = None
    area_in_square_feet: Optional[int] = None
    number_of_floors: Optional[int] = None
    number_of_beds: Optional[int] = None
    licensed_bed_count: Optional[int] = None
    in_house_lab: Optional[bool] = None
    in_house_pharmacy: Optional[bool] = None
    ambulance_service: Optional[bool] = None
    reception: Optional[bool] = None
    tpa_insurance_department: Optional[bool] = None
    patient_counselling_area: Optional[bool] = None
    physiotherapy_department: Optional[bool] = None
    admin_office_present: Optional[bool] = None
    number_of_opds: Optional[int] = None
    number_of_icus: Optional[int] = None
    total_icu_beds: Optional[int] = None
    special_rooms: Optional[int] = None
    semi_special_rooms: Optional[int] = None
    number_of_suites: Optional[int] = None
    number_of_general_wards: Optional[int] = None
    number_of_general_ward_beds: Optional[int] = None
    types_of_operation_theaters: Optional[str] = None
    number_of_operation_theaters: Optional[int] = None
    central_oxygen_supply: Optional[bool] = None
    number_of_ventilators: Optional[int] = None
    infra_equipment_validation: Optional[str] = None
    infrastructure_verified: Optional[bool] = None
    other_infrastructure: Optional[str] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True



class LabCreate(BaseModel):
    hospital_id: Optional[int] = None
    lab_name: Optional[str] = None
    lab_pathologist_name: Optional[str] = None
    lab_pathologist_type: Optional[str] = None
    qualification_of_lab_pathologist: Optional[str] = None
    pathologist_own_lab_name_location: Optional[str] = None
    lab_equipment_available: Optional[bool] = None
    type_of_tests_done: Optional[str] = None
    tests_outsourced: Optional[str] = None
    xray_machine: Optional[bool] = None
    c_arm_machine: Optional[bool] = None
    ct_scan: Optional[bool] = None
    mri_machine: Optional[bool] = None
    usg_machine: Optional[bool] = None
    other_diagnostic_equipment: Optional[str] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True

class PharmacyCreate(BaseModel):
    hospital_id: Optional[int] = None
    pharmacy_name: Optional[str] = None
    pharmacy_drug_license_number: Optional[str] = None
    pharmacy_working_hours: Optional[str] = None
    pharmacist_name: Optional[str] = None
    pharmacist_registration_number: Optional[str] = None
    stock_register: Optional[bool] = None
    purchase_bills: Optional[bool] = None
    sales_register: Optional[bool] = None
    other_pharmacy_documentation: Optional[str] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True



class RegistersProtocolsCreate(BaseModel):
    hospital_id: Optional[int] = None
    ipd_register: Optional[bool] = None
    icu_register: Optional[bool] = None
    opd_register: Optional[bool] = None
    operation_theater_register: Optional[bool] = None
    lab_register: Optional[bool] = None
    mlc_register: Optional[bool] = None
    infection_control_protocols: Optional[bool] = None
    consultant_visits_register: Optional[bool] = None
    salary_slips_available: Optional[bool] = None
    salary_payment_mode: Optional[bool] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True


class FinancialCreate(BaseModel):
    hospital_id: Optional[int] = None
    bank_account_number: Optional[str] = None
    ifsc_code: Optional[str] = None
    cancelled_cheque_copy: Optional[str] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True


class BagicCreate(BaseModel):
    hospital_id: Optional[int] = None
    bagic_to_other_patients_ratio: Optional[str] = None
    average_stay: Optional[int] = None
    surgical_to_medical_packages_ratio: Optional[str] = None
    bagic_mou_copy: Optional[str] = None
    bagic_soc_type: Optional[str] = None
    bagic_empanelment_done_by: Optional[str] = None
    bagic_empanelment_experience: Optional[str] = None
    bagic_claim_approval_experience: Optional[str] = None
    bagic_claim_verification_experience: Optional[str] = None
    bagic_payments_experience: Optional[str] = None
    suggestion_for_bagic: Optional[str] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True

#
# class DigitalEvidenceCreate(BaseModel):
#     hospital_id: Optional[int] = None
#     hospital_photographs: Optional[str] = None
#     hospital_stamp_photo: Optional[str] = None
#     auditor_signature: Optional[str] = None
#     hospital_representative_signature: Optional[str] = None
#     website_url: Optional[str] = None
#     website_valid: Optional[bool] = None
#     suspicious_google_reviews_found: Optional[bool] = None
#     photo_originality_verified: Optional[bool] = None
#     audit_status: Optional[str] = None

class AuditMetadataBase(BaseModel):
    hospital_id: int
    date_of_visit: Optional[date] = None
    visit_done_by: Optional[str] = None
    attended_by: Optional[str] = None
    designation: Optional[str] = None
    information_given_by: Optional[str] = None
    remark_by_auditor: Optional[str] = None
    remark_by_hospital_manager_owner: Optional[str] = None
    hospital_manager_owner_name: Optional[str] = None
    new_setup_claim_verified: Optional[bool] = None
    human_presence_verified: Optional[bool] = None
    local_market_intel_remarks: Optional[str] = None
    repeat_tpa_fraud_suspected: Optional[bool] = None
    audit_status: Optional[str] = None

    class Config:
        from_attributes = True

class FullHospitalData(BaseModel):
    basic_info: Optional[BasicInfoBase] = None
    registration_details: Optional[RegistrationCreate] = None
    empanelment_details: Optional[EmpanelmentCreate] = None
    staff_details: Optional[StaffCreate] = None
    infra_structure_details: Optional[InfrastructureCreate] = None
    lab_details: Optional[LabCreate] = None
    pharmacy_details: Optional[PharmacyCreate] = None
    registers_protocol_details: Optional[RegistersProtocolsCreate] = None
    financial_details: Optional[FinancialCreate] = None
    bagic_details: Optional[BagicCreate] = None
    audit_metadata: Optional[AuditMetadataBase] = None

    class Config:
        from_attributes = True

class FullHospitalDataList(BaseModel):
    hospitals: List[FullHospitalData]
