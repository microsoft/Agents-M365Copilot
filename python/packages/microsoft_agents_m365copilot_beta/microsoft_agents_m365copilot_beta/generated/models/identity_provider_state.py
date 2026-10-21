from enum import Enum

class IdentityProviderState(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

