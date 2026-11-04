from enum import Enum

class AccessDriftResourceType(str, Enum):
    Application = "application",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

