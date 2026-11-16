from enum import Enum

class ApiUsageReportOnboardingStatus(str, Enum):
    Enabling = "enabling",
    Enabled = "enabled",
    Disabling = "disabling",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

