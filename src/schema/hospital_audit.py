from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date
from datetime import datetime
from src.enum import (
    StateEnum, AreaTypeEnum, OwnershipTypeEnum, QualificationEnum,
    HospitalTypeEnum, SpecialtyTypeEnum, YesNoAppliedEnum, WorkingTypeEnum,
    BuildingOwnershipEnum, BuildingTypeEnum, LabPathologistTypeEnum,
    LabPathologistQualificationEnum, YesNoEnum, BagicEmpanelmentByEnum,
    BagicSocTypeEnum, ExperienceRatingEnum
)


class HospitalAuditBase(BaseModel):
    hospital_name: Optional[str] = None
    address: Optional[str] = None
    location_city: Optional[str] = None
    state: Optional[str] = None  # Changed from StateEnum to str
    area_type: Optional[str] = None  # Changed from AreaTypeEnum to str
    hospital_ownership_type: Optional[str] = None  # Changed from OwnershipTypeEnum to str
    run_by: Optional[str] = None
    owned_by: Optional[str] = None
    qualification_of_owner: Optional[str] = None  # Changed from QualificationEnum to str
    hospital_type: Optional[str] = None  # Changed from HospitalTypeEnum to str
    specialty_type: Optional[str] = None  # Changed from SpecialtyTypeEnum to str
    specialty: Optional[str] = None
    specialty_other: Optional[str] = None
    govt_schemes_run: Optional[str] = None
    govt_schemes_run_other: Optional[str] = None
    tpas_empaneled: Optional[str] = None
    tpas_empaneled_other: Optional[str] = None
    insurance_companies_empaneled: Optional[str] = None
    corporates_empaneled: Optional[str] = None

    # Registration fields
    hospital_registration_number: Optional[str] = None
    registered_with: Optional[str] = None
    registration_valid_up_to: Optional[date] = None
    registration_number_of_beds: Optional[int] = None
    mtp_registration: Optional[str] = None
    pndt_registration: Optional[str] = None
    organ_transplant_registration: Optional[str] = None
    nabh_accreditation: Optional[str] = None  # Changed from YesNoAppliedEnum to str
    bio_medical_waste_mgmt_registration: Optional[str] = None
    iso_certification: Optional[str] = None
    other_certifications: Optional[str] = None
    cctv_system: Optional[bool] = None
    security_arrangement: Optional[bool] = None
    fire_safety_registration: Optional[str] = None
    staff_health_insurance_policies: Optional[str] = None
    staff_group_mediclaim_insurer: Optional[str] = None
    other_compliance_documents: Optional[str] = None

    # Staff information - all working_type fields changed from Enum to str
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

    # Staff counts
    number_of_specialist_doctors: Optional[int] = Field(default=0, ge=0)
    number_of_super_specialist_doctors: Optional[int] = Field(default=0, ge=0)
    number_of_mbbs_and_above_doctors: Optional[int] = Field(default=0, ge=0)
    number_of_trained_nurses: Optional[int] = Field(default=0, ge=0)
    number_of_housemen: Optional[int] = Field(default=0, ge=0)
    number_of_resident_doctors: Optional[int] = Field(default=0, ge=0)
    number_of_untrained_nurses: Optional[int] = Field(default=0, ge=0)
    number_of_admin_staff: Optional[int] = Field(default=0, ge=0)
    number_of_other_staff: Optional[int] = Field(default=0, ge=0)
    total_number_of_staff: Optional[int] = Field(default=0, ge=0)

    # Infrastructure
    type_of_building: Optional[str] = None  # Changed from BuildingTypeEnum to str
    number_of_beds: Optional[int] = None
    in_house_lab: Optional[bool] = None
    in_house_pharmacy: Optional[bool] = None
    number_of_opds: Optional[int] = Field(default=0, ge=0)
    number_of_icus: Optional[int] = Field(default=0, ge=0)
    total_icu_beds: Optional[int] = Field(default=0, ge=0)
    special_rooms: Optional[int] = Field(default=0, ge=0)
    semi_special_rooms: Optional[int] = Field(default=0, ge=0)
    number_of_suites: Optional[int] = Field(default=0, ge=0)
    number_of_general_wards: Optional[int] = Field(default=0, ge=0)
    number_of_general_ward_beds: Optional[int] = Field(default=0, ge=0)
    types_of_operation_theaters: Optional[str] = None
    number_of_operation_theaters: Optional[int] = Field(default=0, ge=0)
    central_oxygen_supply: Optional[bool] = None
    number_of_ventilators: Optional[int] = Field(default=0, ge=0)
    area_in_square_feet: Optional[int] = None
    number_of_floors: Optional[int] = None
    building_ownership: Optional[str] = None  # Changed from BuildingOwnershipEnum to str
    ambulance_service: Optional[bool] = None
    reception: Optional[bool] = None
    tpa_insurance_department: Optional[bool] = None
    patient_counselling_area: Optional[bool] = None
    physiotherapy_department: Optional[bool] = None
    other_infrastructure: Optional[str] = None

    # Lab section
    lab_name: Optional[str] = None
    lab_pathologist_name: Optional[str] = None
    lab_pathologist_type: Optional[str] = None  # Changed from LabPathologistTypeEnum to str
    qualification_of_lab_pathologist: Optional[str] = None  # Changed from LabPathologistQualificationEnum to str
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

    # Pharmacy section
    pharmacy_name: Optional[str] = None
    pharmacy_drug_license_number: Optional[str] = None
    pharmacy_working_hours: Optional[str] = None
    pharmacist_name: Optional[str] = None
    pharmacist_registration_number: Optional[str] = None
    stock_register: Optional[bool] = None
    purchase_bills: Optional[bool] = None
    sales_register: Optional[bool] = None
    other_pharmacy_documentation: Optional[str] = None

    # Registers
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

    # BAGIC Section - all changed from Enum to str
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

    # Audit Completion
    date_of_visit: Optional[date] = None
    visit_done_by: Optional[str] = None
    attended_by: Optional[str] = None
    designation: Optional[str] = None
    information_given_by: Optional[str] = None
    remark_by_auditor: Optional[str] = None
    remark_by_hospital_manager_owner: Optional[str] = None
    auditor_signature: Optional[str] = None
    hospital_manager_owner_name: Optional[str] = None
    hospital_representative_signature: Optional[str] = None
    hospital_stamp_photo: Optional[str] = None

    unique_code: Optional[str] = None

    # Add validators to ensure enum values are still valid
    @validator('state')
    def validate_state(cls, v):
        if v is not None:
            try:
                StateEnum(v)
            except ValueError:
                valid_values = [e.value for e in StateEnum]
                raise ValueError(f'Invalid state. Must be one of: {valid_values}')
        return v

    @validator('area_type')
    def validate_area_type(cls, v):
        if v is not None:
            try:
                AreaTypeEnum(v)
            except ValueError:
                valid_values = [e.value for e in AreaTypeEnum]
                raise ValueError(f'Invalid area_type. Must be one of: {valid_values}')
        return v




class HospitalAuditCreate(HospitalAuditBase):
    hospital_name: str = Field(..., min_length=1, max_length=255)


class HospitalAuditUpdate(HospitalAuditBase):
    pass


class HospitalAuditResponse(HospitalAuditBase):
    hosp_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    unique_code: Optional[str] = None

    class Config:
        from_attributes = True