from enum import Enum

class RuleSeverityType(str, Enum):
    Unknown = "unknown",
    Informational = "informational",
    Warning = "warning",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

