from enum import Enum

class CloudAppInfoState(str, Enum):
    True_ = "true",
    False_ = "false",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

