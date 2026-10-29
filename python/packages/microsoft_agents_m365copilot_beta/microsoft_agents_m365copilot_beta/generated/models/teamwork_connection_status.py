from enum import Enum

class TeamworkConnectionStatus(str, Enum):
    Unknown = "unknown",
    Connected = "connected",
    Disconnected = "disconnected",
    UnknownFutureValue = "unknownFutureValue",

