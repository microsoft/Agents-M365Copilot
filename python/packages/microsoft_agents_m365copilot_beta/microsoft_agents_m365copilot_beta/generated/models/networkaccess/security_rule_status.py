from enum import Enum

class SecurityRuleStatus(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    ReportOnly = "reportOnly",
    UnknownFutureValue = "unknownFutureValue",

