from enum import Enum

class AlertStatusType(str, Enum):
    Active = "active",
    Resolved = "resolved",
    UnknownFutureValue = "unknownFutureValue",

