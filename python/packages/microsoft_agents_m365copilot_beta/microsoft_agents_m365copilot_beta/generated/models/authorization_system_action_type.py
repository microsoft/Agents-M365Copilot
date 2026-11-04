from enum import Enum

class AuthorizationSystemActionType(str, Enum):
    Delete = "delete",
    Read = "read",
    UnknownFutureValue = "unknownFutureValue",

