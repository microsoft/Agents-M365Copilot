from enum import Enum

class DeviceAppManagementTaskPriority(str, Enum):
    # No priority set.
    None_ = "none",
    # High priority.
    High = "high",
    # Low priority.
    Low = "low",

