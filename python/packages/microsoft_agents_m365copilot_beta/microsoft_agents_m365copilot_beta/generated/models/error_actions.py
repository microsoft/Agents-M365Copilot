from enum import Enum

class ErrorActions(str, Enum):
    None_ = "none",
    Audit = "audit",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

