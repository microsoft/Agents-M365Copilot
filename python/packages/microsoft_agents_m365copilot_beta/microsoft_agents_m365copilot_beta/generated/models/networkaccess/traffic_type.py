from enum import Enum

class TrafficType(str, Enum):
    Internet = "internet",
    Private = "private",
    Microsoft365 = "microsoft365",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",

