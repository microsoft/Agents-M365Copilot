from enum import Enum

class SkillProficiencyLevel(str, Enum):
    Elementary = "elementary",
    LimitedWorking = "limitedWorking",
    GeneralProfessional = "generalProfessional",
    AdvancedProfessional = "advancedProfessional",
    Expert = "expert",
    UnknownFutureValue = "unknownFutureValue",

