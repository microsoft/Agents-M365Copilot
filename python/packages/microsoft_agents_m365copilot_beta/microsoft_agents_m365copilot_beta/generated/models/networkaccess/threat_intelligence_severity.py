from enum import Enum

class ThreatIntelligenceSeverity(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

