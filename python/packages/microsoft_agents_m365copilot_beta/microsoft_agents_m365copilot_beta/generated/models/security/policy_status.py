from enum import Enum

class PolicyStatus(str, Enum):
    Pending = "pending",
    Error = "error",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

