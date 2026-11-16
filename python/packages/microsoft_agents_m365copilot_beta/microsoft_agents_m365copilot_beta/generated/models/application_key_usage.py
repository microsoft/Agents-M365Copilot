from enum import Enum

class ApplicationKeyUsage(str, Enum):
    Sign = "sign",
    Verify = "verify",
    UnknownFutureValue = "unknownFutureValue",

