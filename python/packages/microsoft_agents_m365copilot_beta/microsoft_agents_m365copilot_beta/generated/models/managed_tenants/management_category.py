from enum import Enum

class ManagementCategory(str, Enum):
    Custom = "custom",
    Devices = "devices",
    Identity = "identity",
    Data = "data",
    UnknownFutureValue = "unknownFutureValue",

