from enum import Enum

class IncidentTaskActionStatus(str, Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    PartiallyCompleted = "partiallyCompleted",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

