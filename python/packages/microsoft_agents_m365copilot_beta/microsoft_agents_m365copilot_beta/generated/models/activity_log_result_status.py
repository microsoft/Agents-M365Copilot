from enum import Enum

class ActivityLogResultStatus(str, Enum):
    Succeeded = "succeeded",
    Failed = "failed",
    PartiallySucceeded = "partiallySucceeded",
    UnknownFutureValue = "unknownFutureValue",

