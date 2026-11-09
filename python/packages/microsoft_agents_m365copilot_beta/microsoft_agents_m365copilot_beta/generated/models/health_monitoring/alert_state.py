from enum import Enum

class AlertState(str, Enum):
    Active = "active",
    Resolved = "resolved",
    UnknownFutureValue = "unknownFutureValue",

