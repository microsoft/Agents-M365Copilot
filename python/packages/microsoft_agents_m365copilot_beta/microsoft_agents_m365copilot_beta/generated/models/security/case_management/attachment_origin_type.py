from enum import Enum

class AttachmentOriginType(str, Enum):
    Case = "case",
    Comment = "comment",
    Task = "task",
    UnknownFutureValue = "unknownFutureValue",

