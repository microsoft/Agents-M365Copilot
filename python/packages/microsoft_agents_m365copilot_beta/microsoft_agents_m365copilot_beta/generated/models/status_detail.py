from enum import Enum

class StatusDetail(str, Enum):
    Submitted = "submitted",
    Approved = "approved",
    Completed = "completed",
    Canceled = "canceled",
    Rejected = "rejected",
    UnknownFutureValue = "unknownFutureValue",

