from enum import Enum

class LifecyclePolicySource(str, Enum):
    UserCreated = "userCreated",
    SystemDefault = "systemDefault",
    UnknownFutureValue = "unknownFutureValue",

