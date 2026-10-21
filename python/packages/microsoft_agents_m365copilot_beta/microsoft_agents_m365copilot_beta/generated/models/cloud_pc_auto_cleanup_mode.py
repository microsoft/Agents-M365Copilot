from enum import Enum

class CloudPcAutoCleanupMode(str, Enum):
    None_ = "none",
    Scheduled = "scheduled",
    OnQuotaExceeded = "onQuotaExceeded",
    UnknownFutureValue = "unknownFutureValue",

