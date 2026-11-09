from enum import Enum

class CloudPcConnectivityEventResult(str, Enum):
    Unknown = "unknown",
    Success = "success",
    Failure = "failure",
    UnknownFutureValue = "unknownFutureValue",

