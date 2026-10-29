from enum import Enum

class ForwardingCategory(str, Enum):
    Default = "default",
    Optimized = "optimized",
    Allow = "allow",
    UnknownFutureValue = "unknownFutureValue",

