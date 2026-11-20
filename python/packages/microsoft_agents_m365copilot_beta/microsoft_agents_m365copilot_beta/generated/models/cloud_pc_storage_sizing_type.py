from enum import Enum

class CloudPcStorageSizingType(str, Enum):
    Dynamic = "dynamic",
    Fixed = "fixed",
    UnknownFutureValue = "unknownFutureValue",

