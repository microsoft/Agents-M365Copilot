from enum import Enum

class ActivityLogSeverity(str, Enum):
    High = "high",
    Medium = "medium",
    Low = "low",
    UnknownFutureValue = "unknownFutureValue",

