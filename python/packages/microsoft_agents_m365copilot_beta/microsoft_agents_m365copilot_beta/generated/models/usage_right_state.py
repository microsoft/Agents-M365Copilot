from enum import Enum

class UsageRightState(str, Enum):
    Active = "active",
    Inactive = "inactive",
    Warning = "warning",
    Suspended = "suspended",
    UnknownFutureValue = "unknownFutureValue",

