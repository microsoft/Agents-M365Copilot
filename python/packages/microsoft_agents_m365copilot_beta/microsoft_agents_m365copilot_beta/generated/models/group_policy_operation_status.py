from enum import Enum

class GroupPolicyOperationStatus(str, Enum):
    # Group Policy unknown operation status.
    Unknown = "unknown",
    # Group Policy in progress operation status.
    InProgress = "inProgress",
    # Group Policy successful operation status.
    Success = "success",
    # Group Policy failed operation status.
    Failed = "failed",

