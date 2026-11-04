from enum import Enum

class SensorStatus(str, Enum):
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",

