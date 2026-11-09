from enum import Enum

class NetworkTrafficOperationStatus(str, Enum):
    Success = "success",
    Failure = "failure",
    UnknownFutureValue = "unknownFutureValue",

