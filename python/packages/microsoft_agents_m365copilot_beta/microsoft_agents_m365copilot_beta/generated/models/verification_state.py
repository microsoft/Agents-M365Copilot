from enum import Enum

class VerificationState(str, Enum):
    Unverified = "unverified",
    Verified = "verified",
    Revoked = "revoked",
    Suspended = "suspended",
    Issued = "issued",
    Blocked = "blocked",
    UnknownFutureValue = "unknownFutureValue",

