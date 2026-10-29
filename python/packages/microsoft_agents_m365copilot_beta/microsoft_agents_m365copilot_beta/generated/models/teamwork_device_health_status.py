from enum import Enum

class TeamworkDeviceHealthStatus(str, Enum):
    Unknown = "unknown",
    Offline = "offline",
    Critical = "critical",
    NonUrgent = "nonUrgent",
    Healthy = "healthy",
    UnknownFutureValue = "unknownFutureValue",

