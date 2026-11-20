from enum import Enum

class ChainBreakSource(str, Enum):
    None_ = "none",
    IdentityProtection = "identityProtection",
    AdminAction = "adminAction",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

