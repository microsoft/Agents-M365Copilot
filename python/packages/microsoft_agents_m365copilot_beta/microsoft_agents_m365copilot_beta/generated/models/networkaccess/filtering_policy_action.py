from enum import Enum

class FilteringPolicyAction(str, Enum):
    Block = "block",
    Allow = "allow",
    UnknownFutureValue = "unknownFutureValue",
    Bypass = "bypass",
    Alert = "alert",

