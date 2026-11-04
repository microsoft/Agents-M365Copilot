from enum import Enum

class PerUserMfaState(str, Enum):
    Disabled = "disabled",
    Enforced = "enforced",
    Enabled = "enabled",
    UnknownFutureValue = "unknownFutureValue",

