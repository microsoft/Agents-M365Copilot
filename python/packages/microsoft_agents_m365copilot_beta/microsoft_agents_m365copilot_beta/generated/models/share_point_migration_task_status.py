from enum import Enum

class SharePointMigrationTaskStatus(str, Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    Cancelled = "cancelled",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

