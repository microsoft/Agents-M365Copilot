from enum import Enum

class AzureAccessType(str, Enum):
    Public = "public",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

