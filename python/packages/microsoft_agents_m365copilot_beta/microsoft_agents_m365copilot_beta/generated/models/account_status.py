from enum import Enum

class AccountStatus(str, Enum):
    Unknown = "unknown",
    Staged = "staged",
    Active = "active",
    Suspended = "suspended",
    Deleted = "deleted",
    UnknownFutureValue = "unknownFutureValue",

