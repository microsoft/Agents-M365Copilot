from enum import Enum

class ApprovalOperationStatus(str, Enum):
    Scheduled = "scheduled",
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    Timeout = "timeout",
    UnknownFutureValue = "unknownFutureValue",

