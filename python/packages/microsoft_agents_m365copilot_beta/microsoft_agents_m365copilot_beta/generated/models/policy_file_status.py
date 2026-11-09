from enum import Enum

class PolicyFileStatus(str, Enum):
    Modified = "modified",
    NotModified = "notModified",
    NoContent = "noContent",
    UnknownFutureValue = "unknownFutureValue",

