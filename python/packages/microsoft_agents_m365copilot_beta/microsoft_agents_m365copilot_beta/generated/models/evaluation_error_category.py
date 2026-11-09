from enum import Enum

class EvaluationErrorCategory(str, Enum):
    Unknown = "unknown",
    SystemLimit = "systemLimit",
    SystemError = "systemError",
    EnforcementError = "enforcementError",
    UnknownFutureValue = "unknownFutureValue",

