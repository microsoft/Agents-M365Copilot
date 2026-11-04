from enum import Enum

class DeviceClientState(str, Enum):
    Offering = "offering",
    OnHold = "onHold",
    Installing = "installing",
    Installed = "installed",
    Cancelled = "cancelled",
    Uninstalling = "uninstalling",
    Uninstalled = "uninstalled",
    NotOffering = "notOffering",
    UnknownFutureValue = "unknownFutureValue",

