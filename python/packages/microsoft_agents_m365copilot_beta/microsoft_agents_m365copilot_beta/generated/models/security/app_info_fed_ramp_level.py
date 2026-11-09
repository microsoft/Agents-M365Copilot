from enum import Enum

class AppInfoFedRampLevel(str, Enum):
    High = "high",
    Moderate = "moderate",
    Low = "low",
    LiSaaS = "liSaaS",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",
    NotSupported = "notSupported",

