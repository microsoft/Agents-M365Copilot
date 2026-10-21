from enum import Enum

class ConnectorHealthState(str, Enum):
    # Indicates a healthy connector status and no action required.
    Healthy = "healthy",
    # Indicates that a connector needs attention.
    Warning = "warning",
    # Indicates that a connector needs immediate attention to retain functionality.
    Unhealthy = "unhealthy",
    # unknown
    Unknown = "unknown",

