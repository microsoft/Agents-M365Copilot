from enum import Enum

class CloudPcProductType(str, Enum):
    Enterprise = "enterprise",
    Frontline = "frontline",
    DevBox = "devBox",
    PowerAutomate = "powerAutomate",
    Business = "business",
    UnknownFutureValue = "unknownFutureValue",

