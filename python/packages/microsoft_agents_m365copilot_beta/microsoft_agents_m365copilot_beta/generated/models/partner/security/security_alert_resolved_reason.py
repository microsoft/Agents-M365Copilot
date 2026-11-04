from enum import Enum

class SecurityAlertResolvedReason(str, Enum):
    Legitimate = "legitimate",
    Ignore = "ignore",
    Fraud = "fraud",
    UnknownFutureValue = "unknownFutureValue",

