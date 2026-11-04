from enum import Enum

class ApprovalState(str, Enum):
    Pending = "pending",
    Approved = "approved",
    Denied = "denied",
    Aborted = "aborted",
    Canceled = "canceled",

