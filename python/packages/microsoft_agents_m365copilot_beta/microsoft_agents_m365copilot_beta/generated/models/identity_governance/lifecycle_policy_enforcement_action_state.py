from enum import Enum

class LifecyclePolicyEnforcementActionState(str, Enum):
    None_ = "none",
    WarningStateEnabled = "warningStateEnabled",
    NonComplianceNotificationSent = "nonComplianceNotificationSent",
    FirstNotificationSent = "firstNotificationSent",
    SecondNotificationSent = "secondNotificationSent",
    FinalNotificationSent = "finalNotificationSent",
    Disabled = "disabled",
    Deleted = "deleted",
    ComplianceRestored = "complianceRestored",
    UnknownFutureValue = "unknownFutureValue",

