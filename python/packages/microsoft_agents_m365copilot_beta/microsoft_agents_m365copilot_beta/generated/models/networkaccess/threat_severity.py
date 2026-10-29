from enum import Enum

class ThreatSeverity(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

