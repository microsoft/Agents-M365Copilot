from enum import Enum

class PlannerApprovalStatus(str, Enum):
    Requested = "requested",
    Approved = "approved",
    Rejected = "rejected",
    Cancelled = "cancelled",
    UnknownFutureValue = "unknownFutureValue",

