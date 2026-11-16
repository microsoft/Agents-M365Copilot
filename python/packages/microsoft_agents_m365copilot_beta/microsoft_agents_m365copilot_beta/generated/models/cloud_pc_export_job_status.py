from enum import Enum

class CloudPcExportJobStatus(str, Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

