from enum import Enum

class HealthState(str, Enum):
    # Unknown state.
    Unknown = "unknown",
    # Healthy state.
    Healthy = "healthy",
    # Unhealthy state.
    Unhealthy = "unhealthy",

