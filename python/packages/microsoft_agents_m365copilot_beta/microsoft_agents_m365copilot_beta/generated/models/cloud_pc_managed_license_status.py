from enum import Enum

class CloudPcManagedLicenseStatus(str, Enum):
    Enabled = "enabled",
    Expired = "expired",
    Blocked = "blocked",
    Deleted = "deleted",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

