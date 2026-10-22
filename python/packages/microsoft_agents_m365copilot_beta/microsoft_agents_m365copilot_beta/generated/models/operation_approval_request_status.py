from enum import Enum

class OperationApprovalRequestStatus(str, Enum):
    # Default. Indicates that the request approval status is unknown, and that the status has not been assigned to the approval request.
    Unknown = "unknown",
    # Indicates that the approval request needs approval before the operation can be completed.
    NeedsApproval = "needsApproval",
    # Indicates that the approval request has been approved. The operation can now be completed.
    Approved = "approved",
    # Indicates that the approval request has been rejected. No further action can be taken to complete the operation or to modify the request.
    Rejected = "rejected",
    # Indicates that the approval request has been cancelled by the request's requestor. No further action can be taken to complete the operation or to modify the request.
    Cancelled = "cancelled",
    # Indicates that the approval request has been completed. This status is feature agnostic and does not indicate success or failure of the operation. No further action is necessary for the operation or to modify the request.
    Completed = "completed",
    # Indicates that the approval request has expired. No further action can be taken to complete the operation or to modify the request. A new approval request must be made and approved in order to complete the operation.
    Expired = "expired",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

