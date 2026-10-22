from enum import Enum

class AppInfoPciDssVersion(str, Enum):
    V1 = "v1",
    V2 = "v2",
    V3 = "v3",
    V3_1 = "v3_1",
    V3_2 = "v3_2",
    V3_2_1 = "v3_2_1",
    NotSupported = "notSupported",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",
    V4 = "v4",

