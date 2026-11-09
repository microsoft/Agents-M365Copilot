from enum import Enum

class ClientFallbackAction(str, Enum):
    Bypass = "bypass",
    Block = "block",
    Default = "default",
    UnknownFutureValue = "unknownFutureValue",

