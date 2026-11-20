from enum import Enum

class ConnectionStatus(str, Enum):
    Open = "open",
    Active = "active",
    Closed = "closed",
    UnknownFutureValue = "unknownFutureValue",

