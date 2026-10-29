from enum import Enum

class PolicyScope(str, Enum):
    None_ = "none",
    All = "all",
    Selected = "selected",
    UnknownFutureValue = "unknownFutureValue",

