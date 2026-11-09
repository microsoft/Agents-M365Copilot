from enum import Enum

class LongRunningOperationStatus(str, Enum):
    NotStarted = "notStarted",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",
    Skipped = "skipped",
    UnknownFutureValue = "unknownFutureValue",

