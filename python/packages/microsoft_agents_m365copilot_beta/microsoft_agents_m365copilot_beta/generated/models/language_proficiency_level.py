from enum import Enum

class LanguageProficiencyLevel(str, Enum):
    Elementary = "elementary",
    Conversational = "conversational",
    LimitedWorking = "limitedWorking",
    ProfessionalWorking = "professionalWorking",
    FullProfessional = "fullProfessional",
    NativeOrBilingual = "nativeOrBilingual",
    UnknownFutureValue = "unknownFutureValue",

