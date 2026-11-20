from enum import Enum

class TokenProtectionStatus(str, Enum):
    None_ = "none",
    Bound = "bound",
    Unbound = "unbound",
    UnknownFutureValue = "unknownFutureValue",

