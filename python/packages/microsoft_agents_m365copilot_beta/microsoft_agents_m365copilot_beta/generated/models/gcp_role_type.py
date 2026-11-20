from enum import Enum

class GcpRoleType(str, Enum):
    System = "system",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

