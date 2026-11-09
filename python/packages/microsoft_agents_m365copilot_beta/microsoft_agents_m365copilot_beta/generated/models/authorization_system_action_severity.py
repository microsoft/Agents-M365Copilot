from enum import Enum

class AuthorizationSystemActionSeverity(str, Enum):
    Normal = "normal",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

