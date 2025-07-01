import enum

class StateEnum(str, enum.Enum):
    Andhra_Pradesh = 'Andhra Pradesh'
    Arunachal_Pradesh = 'Arunachal Pradesh'
    Assam = 'Assam'
    Bihar = 'Bihar'
    Chhattisgarh = 'Chhattisgarh'
    Goa = 'Goa'
    Gujarat = 'Gujarat'
    Haryana = 'Haryana'
    Himachal_Pradesh = 'Himachal Pradesh'
    Jharkhand = 'Jharkhand'
    Karnataka = 'Karnataka'
    Kerala = 'Kerala'
    Madhya_Pradesh = 'Madhya Pradesh'
    Maharashtra = 'Maharashtra'
    Manipur = 'Manipur'
    Meghalaya = 'Meghalaya'
    Mizoram = 'Mizoram'
    Nagaland = 'Nagaland'
    Odisha = 'Odisha'
    Punjab = 'Punjab'
    Rajasthan = 'Rajasthan'
    Sikkim = 'Sikkim'
    Tamil_Nadu = 'Tamil Nadu'
    Telangana = 'Telangana'
    Tripura = 'Tripura'
    Uttar_Pradesh = 'Uttar Pradesh'
    Uttarakhand = 'Uttarakhand'
    West_Bengal = 'West Bengal'
    Delhi = 'Delhi'
    Jammu_and_Kashmir = 'Jammu and Kashmir'
    Ladakh = 'Ladakh'
    Chandigarh = 'Chandigarh'
    Dadra_Nagar_Haveli_Daman_Diu = 'Dadra and Nagar Haveli and Daman and Diu'
    Lakshadweep = 'Lakshadweep'
    Puducherry = 'Puducherry'

class AreaTypeEnum(str, enum.Enum):
    Urban = 'Urban'
    Semi_Urban = 'Semi-Urban'
    Rural = 'Rural'

class OwnershipTypeEnum(str, enum.Enum):
    Government = 'Government'
    Private = 'Private'
    Trust = 'Trust'
    Society = 'Society'
    Corporate = 'Corporate'
    Partnership = 'Partnership'
    Proprietorship = 'Proprietorship'

class QualificationEnum(str, enum.Enum):
    MBBS = 'MBBS'
    MD = 'MD'
    MS = 'MS'
    DM = 'DM'
    MCh = 'MCh'
    Diploma = 'Diploma'
    BDS = 'BDS'
    MDS = 'MDS'
    BAMS = 'BAMS'
    BHMS = 'BHMS'
    Other_Medical = 'Other Medical'
    Non_Medical = 'Non-Medical'
    Engineer = 'Engineer'
    MBA = 'MBA'
    CA = 'CA'
    Other = 'Other'

class HospitalTypeEnum(str, enum.Enum):
    General = 'General'
    Super_Specialty = 'Super Specialty'
    Multi_Specialty = 'Multi Specialty'
    Single_Specialty = 'Single Specialty'
    Nursing_Home = 'Nursing Home'
    Clinic = 'Clinic'
    Day_Care = 'Day Care'
    Trauma_Center = 'Trauma Center'

class SpecialtyTypeEnum(str, enum.Enum):
    Primary_Care = 'Primary Care'
    Secondary_Care = 'Secondary Care'
    Tertiary_Care = 'Tertiary Care'

class YesNoAppliedEnum(str, enum.Enum):
    Yes = "Yes"
    No = "No"
    Applied = "Applied"

class WorkingTypeEnum(str, enum.Enum):
    Full_Time = "Full Time"
    Part_Time = "Part Time"
    Consultant = "Consultant"
    Visiting = "Visiting"

class BuildingTypeEnum(str, enum.Enum):
    Own_Building = "Own Building"
    Rented = "Rented"
    Leased = "Leased"
    Government_Allotted = "Government Allotted"

class BuildingOwnershipEnum(str, enum.Enum):
    Owned = "Owned"
    Rented = "Rented"
    Leased = "Leased"

class LabPathologistTypeEnum(str, enum.Enum):
    Full_Time = "Full Time"
    Part_Time = "Part Time"
    Visiting = "Visiting"
    Consultant = "Consultant"

class LabPathologistQualificationEnum(str, enum.Enum):
    MD_Pathology = "MD Pathology"
    DCP = "DCP"
    DMLT = "DMLT"
    BMLT = "BMLT"
    MSc_MLT = "MSc MLT"
    Other = "Other"

class YesNoEnum(str, enum.Enum):
    Yes = "Yes"
    No = "No"

class BagicSocTypeEnum(str, enum.Enum):
    Type_A = "Type A"
    Type_B = "Type B"
    Type_C = "Type C"

class BagicEmpanelmentByEnum(str, enum.Enum):
    Direct = "Direct"
    Through_Agent = "Through Agent"
    Through_Consultant = "Through Consultant"

class ExperienceRatingEnum(str, enum.Enum):
    Excellent = "Excellent"
    Good = "Good"
    Average = "Average"
    Poor = "Poor"

