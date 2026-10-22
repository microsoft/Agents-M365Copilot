from enum import Enum

class ConnectivityState(str, Enum):
    Pending = "pending",
    Connected = "connected",
    Inactive = "inactive",
    Error = "error",
    UnknownFutureValue = "unknownFutureValue",

