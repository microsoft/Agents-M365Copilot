from enum import Enum

class EvaluationResultType(str, Enum):
    Unknown = "unknown",
    Success = "success",
    Error = "error",
    NeedAdditionalClaims = "needAdditionalClaims",
    Rejected = "rejected",
    TimedOut = "timedOut",
    CapacityExceeded = "capacityExceeded",
    UnknownFutureValue = "unknownFutureValue",

