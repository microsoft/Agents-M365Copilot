from enum import Enum

class AssigneeTypes(str, Enum):
    None_ = "none",
    User = "user",
    Group = "group",
    Device = "device",
    UnknownFutureValue = "unknownFutureValue",

