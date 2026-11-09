from enum import Enum

class HotpatchReadiness(str, Enum):
    Ready = "ready",
    NotReady = "notReady",
    UnknownFutureValue = "unknownFutureValue",

