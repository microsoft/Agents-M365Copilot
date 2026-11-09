from enum import Enum

class PlannerTaskStatus(str, Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    Blocked = "blocked",
    UnknownFutureValue = "unknownFutureValue",

