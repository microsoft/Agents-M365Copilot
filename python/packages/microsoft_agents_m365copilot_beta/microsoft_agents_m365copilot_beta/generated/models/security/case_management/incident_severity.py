from enum import Enum

class IncidentSeverity(str, Enum):
    Unknown = "unknown",
    Informational = "informational",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

