from enum import Enum

class IamStatus(str, Enum):
    Active = "active",
    Inactive = "inactive",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

