from enum import Enum

class IncidentTaskStatus(str, Enum):
    Open = "open",
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    NotRelevant = "notRelevant",
    UnknownFutureValue = "unknownFutureValue",

