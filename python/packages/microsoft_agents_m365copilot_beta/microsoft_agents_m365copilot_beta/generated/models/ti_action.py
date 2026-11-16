from enum import Enum

class TiAction(str, Enum):
    Unknown = "unknown",
    Allow = "allow",
    Block = "block",
    Alert = "alert",
    UnknownFutureValue = "unknownFutureValue",

