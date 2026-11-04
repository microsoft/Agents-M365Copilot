from enum import Enum

class LifecyclePolicyNextEnforcementAction(str, Enum):
    NonComplianceNotification = "nonComplianceNotification",
    FirstNotification = "firstNotification",
    SecondNotification = "secondNotification",
    FinalNotification = "finalNotification",
    Disable = "disable",
    DisableNotification = "disableNotification",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

