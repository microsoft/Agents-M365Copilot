from enum import Enum

class VpnDeadPeerDetectionRate(str, Enum):
    # Medium
    Medium = "medium",
    # None
    None_ = "none",
    # Low
    Low = "low",
    # High
    High = "high",

