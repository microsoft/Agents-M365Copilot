from enum import Enum

class CloudPcServicePlanType(str, Enum):
    Enterprise = "enterprise",
    Business = "business",
    UnknownFutureValue = "unknownFutureValue",

