from enum import Enum

class SubscriptionState(str, Enum):
    Active = "active",
    Warning = "warning",
    Suspended = "suspended",
    LockedOut = "lockedOut",
    Deleted = "deleted",
    UnknownFutureValue = "unknownFutureValue",

