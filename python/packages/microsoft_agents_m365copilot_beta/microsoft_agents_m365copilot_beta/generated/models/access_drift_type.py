from enum import Enum

class AccessDriftType(str, Enum):
    Unauthorized = "unauthorized",
    Missing = "missing",
    InSync = "inSync",
    UnknownFutureValue = "unknownFutureValue",

