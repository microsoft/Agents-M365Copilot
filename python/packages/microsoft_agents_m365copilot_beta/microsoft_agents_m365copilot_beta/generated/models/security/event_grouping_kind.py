from enum import Enum

class EventGroupingKind(str, Enum):
    AlertPerEvent = "alertPerEvent",
    SingleAlert = "singleAlert",
    UnknownFutureValue = "unknownFutureValue",

