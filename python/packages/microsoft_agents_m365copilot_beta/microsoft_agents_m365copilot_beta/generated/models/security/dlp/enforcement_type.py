from enum import Enum

class EnforcementType(str, Enum):
    Unknown = "unknown",
    Combined = "combined",
    Separate = "separate",
    UnknownFutureValue = "unknownFutureValue",

