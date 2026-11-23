from enum import Enum

class ResourcePolicyDecision(str, Enum):
    Deny = "deny",
    None_ = "none",
    Compliant = "compliant",
    UnknownFutureValue = "unknownFutureValue",

