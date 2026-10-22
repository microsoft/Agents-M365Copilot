from enum import Enum

class EvaluationState(str, Enum):
    Unknown = "unknown",
    Created = "created",
    Running = "running",
    Completed = "completed",
    Cancelled = "cancelled",
    Pending = "pending",
    Deferred = "deferred",
    WaitingForInput = "waitingForInput",
    UnknownFutureValue = "unknownFutureValue",

