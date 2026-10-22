from enum import Enum

class AppManagementAuditLogPolicyType(str, Enum):
    DefaultEntraId = "defaultEntraId",
    Tenant = "tenant",
    App = "app",
    UnknownFutureValue = "unknownFutureValue",

