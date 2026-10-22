from enum import Enum

class CaseTaskPriority(str, Enum):
    NotSet = "notSet",
    VeryLow = "veryLow",
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

