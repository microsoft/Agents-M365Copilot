from enum import Enum

class EntityType(str, Enum):
    UserName = "userName",
    IpAddress = "ipAddress",
    MachineName = "machineName",
    Other = "other",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

