from enum import Enum

class TeamworkDeviceActivityState(str, Enum):
    Unknown = "unknown",
    Busy = "busy",
    Idle = "idle",
    Unavailable = "unavailable",
    UnknownFutureValue = "unknownFutureValue",

