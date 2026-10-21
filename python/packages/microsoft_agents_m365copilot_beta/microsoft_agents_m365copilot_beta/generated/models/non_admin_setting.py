from enum import Enum

class NonAdminSetting(str, Enum):
    False_ = "false",
    True_ = "true",
    UnknownFutureValue = "unknownFutureValue",

