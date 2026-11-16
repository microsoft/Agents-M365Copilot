from enum import Enum

class DeviceServiceState(str, Enum):
    Unknown = "unknown",
    Pending = "pending",
    Offering = "offering",
    OnHold = "onHold",
    Cancelled = "cancelled",
    NotOffering = "notOffering",
    UnknownFutureValue = "unknownFutureValue",

