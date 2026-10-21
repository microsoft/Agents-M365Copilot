from enum import Enum

class CloudPcUserAccessLevel(str, Enum):
    Unrestricted = "unrestricted",
    Restricted = "restricted",
    UnknownFutureValue = "unknownFutureValue",

