from enum import Enum

class ServicePrincipalLockScope(str, Enum):
    NotConfigured = "notConfigured",
    ForeignTenantOnly = "foreignTenantOnly",
    Everywhere = "everywhere",
    UnknownFutureValue = "unknownFutureValue",

