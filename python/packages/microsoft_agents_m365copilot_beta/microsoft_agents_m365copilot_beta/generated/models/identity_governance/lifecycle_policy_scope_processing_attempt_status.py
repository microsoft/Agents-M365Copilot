from enum import Enum

class LifecyclePolicyScopeProcessingAttemptStatus(str, Enum):
    NotStarted = "notStarted",
    Evaluating = "evaluating",
    Processing = "processing",
    Completed = "completed",
    Failed = "failed",
    TimedOut = "timedOut",
    InvalidScope = "invalidScope",
    UnknownFutureValue = "unknownFutureValue",

