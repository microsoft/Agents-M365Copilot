from enum import Enum

class DocumentProcessingJobStatus(str, Enum):
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

