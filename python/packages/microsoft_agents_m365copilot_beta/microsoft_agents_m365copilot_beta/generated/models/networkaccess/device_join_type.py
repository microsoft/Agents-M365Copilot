from enum import Enum

class DeviceJoinType(str, Enum):
    None_ = "none",
    MicrosoftEntraJoined = "microsoftEntraJoined",
    MicrosoftEntraRegistered = "microsoftEntraRegistered",
    UnknownFutureValue = "unknownFutureValue",

