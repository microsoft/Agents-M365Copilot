from enum import Enum

class TrustFrameworkKeyStatus(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

