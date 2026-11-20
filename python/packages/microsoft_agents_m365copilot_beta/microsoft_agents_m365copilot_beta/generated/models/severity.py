from enum import Enum

class Severity(str, Enum):
    None_ = "none",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

