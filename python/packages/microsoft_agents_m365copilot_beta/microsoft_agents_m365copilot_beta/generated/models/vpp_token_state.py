from enum import Enum

class VppTokenState(str, Enum):
    # Default state.
    Unknown = "unknown",
    # Token is valid.
    Valid = "valid",
    # Token is expired.
    Expired = "expired",
    # Token is invalid.
    Invalid = "invalid",
    # Token is managed by another MDM Service.
    AssignedToExternalMDM = "assignedToExternalMDM",
    # Token is associated with the same location as another token on the account.
    DuplicateLocationId = "duplicateLocationId",

