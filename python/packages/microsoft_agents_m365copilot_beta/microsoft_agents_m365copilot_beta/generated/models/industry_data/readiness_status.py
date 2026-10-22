from enum import Enum

class ReadinessStatus(str, Enum):
    NotReady = "notReady",
    Ready = "ready",
    Failed = "failed",
    Disabled = "disabled",
    Expired = "expired",
    UnknownFutureValue = "unknownFutureValue",

