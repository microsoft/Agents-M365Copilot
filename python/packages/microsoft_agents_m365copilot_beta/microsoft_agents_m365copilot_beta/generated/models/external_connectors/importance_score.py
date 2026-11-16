from enum import Enum

class ImportanceScore(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    VeryHigh = "veryHigh",
    UnknownFutureValue = "unknownFutureValue",

