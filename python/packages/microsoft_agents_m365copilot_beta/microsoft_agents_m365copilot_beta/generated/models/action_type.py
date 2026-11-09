from enum import Enum

class ActionType(str, Enum):
    Tunnel = "tunnel",
    Exclude = "exclude",
    UnknownFutureValue = "unknownFutureValue",

