from enum import Enum

class ApprovedBy(str, Enum):
    System = "system",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",

