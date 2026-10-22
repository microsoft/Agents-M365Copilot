from enum import Enum

class Kind(str, Enum):
    Unrestricted = "unrestricted",
    AllowedTenants = "allowedTenants",
    UnknownFutureValue = "unknownFutureValue",

