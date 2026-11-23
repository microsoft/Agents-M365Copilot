from enum import Enum

class VerificationLifecycleSource(str, Enum):
    Entra = "entra",
    AdminOverride = "adminOverride",
    ApiOverride = "apiOverride",
    UnknownFutureValue = "unknownFutureValue",

