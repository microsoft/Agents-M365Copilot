from enum import Enum

class PolicyStatus(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

