from enum import Enum

class DeviceCategory(str, Enum):
    Client = "client",
    Branch = "branch",
    UnknownFutureValue = "unknownFutureValue",
    RemoteNetwork = "remoteNetwork",

