from enum import Enum

class AppManagementAuditLogRestrictionResult(str, Enum):
    Allowed = "allowed",
    Blocked = "blocked",
    UnknownFutureValue = "unknownFutureValue",

