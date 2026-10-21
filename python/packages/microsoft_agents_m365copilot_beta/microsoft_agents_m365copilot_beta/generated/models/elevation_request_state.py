from enum import Enum

class ElevationRequestState(str, Enum):
    # Default Value. Indicates that elevation request status is unavailable
    None_ = "none",
    # Initial state when request is submitted but no approval/denial action taken
    Pending = "pending",
    # Indicates elevation request has been approved by IT Admin.
    Approved = "approved",
    # Indicates elevation request has been denied by IT Admin.
    Denied = "denied",
    # Set to expire when Approved for is elapsed or ExpireDate is elapsed, whichever is sooner.
    Expired = "expired",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Set to expire when Approved for is elapsed or ExpireDate is elapsed, whichever is sooner.
    Revoked = "revoked",
    # Indicates an elevation request that was previously approved and expired has been completed.
    Completed = "completed",

