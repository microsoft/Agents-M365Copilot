from enum import Enum

class LifecyclePolicyEnforcementStatus(str, Enum):
    NotRequired = "notRequired",
    NotStarted = "notStarted",
    Processing = "processing",
    Waiting = "waiting",
    ActionDue = "actionDue",
    Complete = "complete",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

