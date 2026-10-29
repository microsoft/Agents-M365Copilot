from enum import Enum

class ApprovalStatus(str, Enum):
    Approved = "approved",
    Suspended = "suspended",
    UnknownFutureValue = "unknownFutureValue",

