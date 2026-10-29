from enum import Enum

class CloudPcSnapshotHealthCheckStatus(str, Enum):
    Unknown = "unknown",
    Healthy = "healthy",
    Unhealthy = "unhealthy",
    UnknownFutureValue = "unknownFutureValue",

