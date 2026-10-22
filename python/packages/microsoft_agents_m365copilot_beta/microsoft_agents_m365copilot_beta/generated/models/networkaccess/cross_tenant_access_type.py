from enum import Enum

class CrossTenantAccessType(str, Enum):
    None_ = "none",
    B2bCollaboration = "b2bCollaboration",
    UnknownFutureValue = "unknownFutureValue",

