from enum import Enum

class ConditionalAccessAgentIdRiskLevels(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

