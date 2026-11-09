from enum import Enum

class PrivilegeLevel(str, Enum):
    Standard = "standard",
    Privileged = "privileged",
    UnknownFutureValue = "unknownFutureValue",

