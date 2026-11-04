from enum import Enum

class CloudPcExternalPartnerStatus(str, Enum):
    NotAvailable = "notAvailable",
    Available = "available",
    Healthy = "healthy",
    Unhealthy = "unhealthy",
    UnknownFutureValue = "unknownFutureValue",

