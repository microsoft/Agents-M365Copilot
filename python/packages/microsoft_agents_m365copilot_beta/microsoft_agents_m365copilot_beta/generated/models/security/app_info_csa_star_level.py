from enum import Enum

class AppInfoCsaStarLevel(str, Enum):
    SelfAssessment = "selfAssessment",
    Certification = "certification",
    Attestation = "attestation",
    CStarAssessment = "cStarAssessment",
    ContinuousMonitoring = "continuousMonitoring",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

