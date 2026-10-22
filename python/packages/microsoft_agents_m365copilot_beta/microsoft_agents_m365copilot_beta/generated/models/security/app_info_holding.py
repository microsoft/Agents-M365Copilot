from enum import Enum

class AppInfoHolding(str, Enum):
    Private = "private",
    Public = "public",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

