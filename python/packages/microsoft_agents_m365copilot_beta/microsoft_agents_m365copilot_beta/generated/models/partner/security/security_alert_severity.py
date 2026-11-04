from enum import Enum

class SecurityAlertSeverity(str, Enum):
    Informational = "informational",
    High = "high",
    Medium = "medium",
    Low = "low",
    UnknownFutureValue = "unknownFutureValue",

