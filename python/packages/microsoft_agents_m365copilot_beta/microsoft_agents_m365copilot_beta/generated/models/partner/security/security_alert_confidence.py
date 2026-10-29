from enum import Enum

class SecurityAlertConfidence(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

