from enum import Enum

class TrafficForwardingType(str, Enum):
    M365 = "m365",
    Internet = "internet",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

