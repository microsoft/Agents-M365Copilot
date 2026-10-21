from enum import Enum

class PolicySetStatus(str, Enum):
    # Default Value.
    Unknown = "unknown",
    # All PolicySet items are now validating for corresponding settings of workloads.
    Validating = "validating",
    # Post process complete for all PolicySet items but there are failures.
    PartialSuccess = "partialSuccess",
    # All PolicySet items are deployed. Doesn’t mean that all deployment succeeded. 
    Success = "success",
    # PolicySet processing completely failed.
    Error = "error",
    # PolicySet/PolicySetItem is not assigned to any group.
    NotAssigned = "notAssigned",

