from enum import Enum

class CloudPcConnectivityStatus(str, Enum):
    Unknown = "unknown",
    Available = "available",
    AvailableWithWarning = "availableWithWarning",
    Unavailable = "unavailable",
    UnknownFutureValue = "unknownFutureValue",
    UnderServiceMaintenance = "underServiceMaintenance",
    InUse = "inUse",

