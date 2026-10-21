from enum import Enum

class RecommendationPriority(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

