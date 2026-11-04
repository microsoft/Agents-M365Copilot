from enum import Enum

class HardwareOathTokenStatus(str, Enum):
    Available = "available",
    Assigned = "assigned",
    Activated = "activated",
    FailedActivation = "failedActivation",
    UnknownFutureValue = "unknownFutureValue",

