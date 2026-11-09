from enum import Enum

class WorkloadActionStatus(str, Enum):
    ToAddress = "toAddress",
    Completed = "completed",
    Error = "error",
    TimeOut = "timeOut",
    InProgress = "inProgress",
    UnknownFutureValue = "unknownFutureValue",

