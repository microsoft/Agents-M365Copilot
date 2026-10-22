from enum import Enum

class MembershipRuleProcessingStatusDetails(str, Enum):
    NotStarted = "NotStarted",
    Running = "Running",
    Failed = "Failed",
    Succeeded = "Succeeded",
    UnsupportedFutureValue = "UnsupportedFutureValue",

