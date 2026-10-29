from enum import Enum

class DeviceAppManagementTaskStatus(str, Enum):
    # State is undefined.
    Unknown = "unknown",
    # The task is ready for review.
    Pending = "pending",
    # The task has been accepted and is being worked on.
    Active = "active",
    # The work is complete.
    Completed = "completed",
    # The task was rejected.
    Rejected = "rejected",

