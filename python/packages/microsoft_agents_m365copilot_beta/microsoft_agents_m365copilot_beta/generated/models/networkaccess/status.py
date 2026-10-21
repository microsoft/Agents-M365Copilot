from enum import Enum

class Status(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

