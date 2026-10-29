from enum import Enum

class TaskStatus(str, Enum):
    NotSet = "notSet",
    New = "new",
    InProgress = "inProgress",
    Failed = "failed",
    PartiallyCompleted = "partiallyCompleted",
    Skipped = "skipped",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

