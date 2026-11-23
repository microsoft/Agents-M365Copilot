from enum import Enum

class VerificationEventLifecycleState(str, Enum):
    Active = "active",
    Revoked = "revoked",
    Suspended = "suspended",
    Invalidated = "invalidated",
    Issued = "issued",
    Blocked = "blocked",
    UnknownFutureValue = "unknownFutureValue",

