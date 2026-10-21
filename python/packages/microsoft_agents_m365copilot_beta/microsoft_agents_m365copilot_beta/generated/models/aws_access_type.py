from enum import Enum

class AwsAccessType(str, Enum):
    Public = "public",
    Restricted = "restricted",
    CrossAccount = "crossAccount",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

