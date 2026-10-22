from enum import Enum

class CloudPcSupportedRegionStatus(str, Enum):
    Available = "available",
    Restricted = "restricted",
    Unavailable = "unavailable",
    UnknownFutureValue = "unknownFutureValue",

