from enum import Enum

class ApprovalItemState(str, Enum):
    Canceled = "canceled",
    Created = "created",
    Pending = "pending",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

