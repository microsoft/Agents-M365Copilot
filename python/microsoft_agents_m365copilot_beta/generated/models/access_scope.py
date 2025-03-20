from enum import Enum

class AccessScope(str, Enum):
    InOrganization = "inOrganization",
    NotInOrganization = "notInOrganization",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

