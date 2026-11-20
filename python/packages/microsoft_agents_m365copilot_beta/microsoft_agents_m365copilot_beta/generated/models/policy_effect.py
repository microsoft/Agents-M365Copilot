from enum import Enum

class PolicyEffect(str, Enum):
    Compliant = "compliant",
    Deny = "deny",
    UnknownFutureValue = "unknownFutureValue",

