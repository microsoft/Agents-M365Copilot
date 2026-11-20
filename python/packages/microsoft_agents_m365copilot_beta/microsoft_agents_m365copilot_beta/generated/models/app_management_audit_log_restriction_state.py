from enum import Enum

class AppManagementAuditLogRestrictionState(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    Audit = "audit",
    UnknownFutureValue = "unknownFutureValue",

