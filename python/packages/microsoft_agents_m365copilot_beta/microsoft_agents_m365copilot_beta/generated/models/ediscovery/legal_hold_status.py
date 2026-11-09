from enum import Enum

class LegalHoldStatus(str, Enum):
    Pending = "Pending",
    Error = "Error",
    Success = "Success",
    UnknownFutureValue = "UnknownFutureValue",

