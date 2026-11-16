from enum import Enum

class TenantOnboardingStatus(str, Enum):
    Ineligible = "ineligible",
    InProcess = "inProcess",
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",
    Disabled = "disabled",

