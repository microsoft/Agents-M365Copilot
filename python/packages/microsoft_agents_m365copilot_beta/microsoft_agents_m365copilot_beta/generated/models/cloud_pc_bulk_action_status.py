from enum import Enum

class CloudPcBulkActionStatus(str, Enum):
    Pending = "pending",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

