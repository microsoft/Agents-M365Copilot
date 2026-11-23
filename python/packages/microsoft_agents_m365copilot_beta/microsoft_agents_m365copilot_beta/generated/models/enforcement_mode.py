from enum import Enum

class EnforcementMode(str, Enum):
    DoNotEnforce = "doNotEnforce",
    Enforce = "enforce",
    UnknownFutureValue = "unknownFutureValue",

