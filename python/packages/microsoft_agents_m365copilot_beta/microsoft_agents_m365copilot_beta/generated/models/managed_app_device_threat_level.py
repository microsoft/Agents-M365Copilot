from enum import Enum

class ManagedAppDeviceThreatLevel(str, Enum):
    # Value not configured
    NotConfigured = "notConfigured",
    # Device needs to have no threat
    Secured = "secured",
    # Device needs to have a low threat.
    Low = "low",
    # Device needs to have not more than medium threat.
    Medium = "medium",
    # Device needs to have not more than high threat
    High = "high",

