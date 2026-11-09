from enum import Enum

class TrafficRoutingMethod(str, Enum):
    None_ = "none",
    Random = "random",
    SessionPersistence = "sessionPersistence",
    Performance = "performance",
    UnknownFutureValue = "unknownFutureValue",

