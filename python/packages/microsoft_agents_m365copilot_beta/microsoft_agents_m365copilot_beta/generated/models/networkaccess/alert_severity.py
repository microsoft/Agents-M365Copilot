from enum import Enum

class AlertSeverity(str, Enum):
    Informational = "informational",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

