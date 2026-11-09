from enum import Enum

class HuntingRuleRunStatus(str, Enum):
    Running = "running",
    Completed = "completed",
    Failed = "failed",
    PartiallyFailed = "partiallyFailed",
    UnknownFutureValue = "unknownFutureValue",

