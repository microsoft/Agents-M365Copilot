from enum import Enum

class ActivityStatus(str, Enum):
    NotStarted = "notStarted",
    Running = "running",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

