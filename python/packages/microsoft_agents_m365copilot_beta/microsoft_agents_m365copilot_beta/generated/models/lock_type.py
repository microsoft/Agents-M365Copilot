from enum import Enum

class LockType(str, Enum):
    None_ = "none",
    Exclusive = "exclusive",
    Shared = "shared",
    UnknownFutureValue = "unknownFutureValue",

