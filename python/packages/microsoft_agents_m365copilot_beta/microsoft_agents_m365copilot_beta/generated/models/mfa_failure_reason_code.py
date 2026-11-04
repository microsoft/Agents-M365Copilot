from enum import Enum

class MfaFailureReasonCode(str, Enum):
    MfaIncomplete = "mfaIncomplete",
    MfaDenied = "mfaDenied",
    SystemFailure = "systemFailure",
    BadRequest = "badRequest",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

