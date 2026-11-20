from enum import Enum

class LifecyclePolicyScopeProcessingStatus(str, Enum):
    Idle = "idle",
    NotStarted = "notStarted",
    Evaluating = "evaluating",
    Processing = "processing",
    UnknownFutureValue = "unknownFutureValue",

