from enum import Enum

class SecurityAlertStatus(str, Enum):
    Active = "active",
    Resolved = "resolved",
    Investigating = "investigating",
    UnknownFutureValue = "unknownFutureValue",

