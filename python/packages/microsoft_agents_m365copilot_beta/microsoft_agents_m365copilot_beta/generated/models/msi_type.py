from enum import Enum

class MsiType(str, Enum):
    None_ = "none",
    UserAssigned = "userAssigned",
    SystemAssigned = "systemAssigned",
    UnknownFutureValue = "unknownFutureValue",

