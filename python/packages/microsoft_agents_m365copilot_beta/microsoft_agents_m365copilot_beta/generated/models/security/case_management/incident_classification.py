from enum import Enum

class IncidentClassification(str, Enum):
    Unknown = "unknown",
    FalsePositive = "falsePositive",
    TruePositive = "truePositive",
    InformationalExpectedActivity = "informationalExpectedActivity",
    UnknownFutureValue = "unknownFutureValue",

