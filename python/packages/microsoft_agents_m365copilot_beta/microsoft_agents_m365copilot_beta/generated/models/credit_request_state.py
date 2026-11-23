from enum import Enum

class CreditRequestState(str, Enum):
    # The request is awaiting an administrator decision.
    Pending = "pending",
    # The request has been approved by an administrator.
    Approved = "approved",
    # The request has been rejected by an administrator.
    Rejected = "rejected",
    # The request was cancelled by the system or the requester. Read-only historical state.
    Cancelled = "cancelled",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

