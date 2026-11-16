from enum import Enum

class PlaceOperationStatus(str, Enum):
    Created = "created",
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    PartiallySucceeded = "partiallySucceeded",
    Expired = "expired",
    UnknownFutureValue = "unknownFutureValue",

