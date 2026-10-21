from enum import Enum

class PurposeType(str, Enum):
    Audit = "audit",
    Di = "di",
    UnknownFutureValue = "unknownFutureValue",

