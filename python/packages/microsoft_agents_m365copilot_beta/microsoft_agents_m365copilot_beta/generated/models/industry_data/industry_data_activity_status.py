from enum import Enum

class IndustryDataActivityStatus(str, Enum):
    InProgress = "inProgress",
    Skipped = "skipped",
    Failed = "failed",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    CompletedWithWarnings = "completedWithWarnings",
    UnknownFutureValue = "unknownFutureValue",

