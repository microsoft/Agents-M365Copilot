from enum import Enum

class GroupPrivacy(str, Enum):
    Unspecified = "unspecified",
    Public = "public",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

