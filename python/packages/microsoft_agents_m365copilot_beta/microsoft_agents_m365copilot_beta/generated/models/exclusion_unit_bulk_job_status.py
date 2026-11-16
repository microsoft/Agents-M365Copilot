from enum import Enum

class ExclusionUnitBulkJobStatus(str, Enum):
    Created = "created",
    Active = "active",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    UnknownFutureValue = "unknownFutureValue",

