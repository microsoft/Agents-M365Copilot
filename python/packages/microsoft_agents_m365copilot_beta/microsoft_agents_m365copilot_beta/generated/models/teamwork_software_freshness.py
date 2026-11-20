from enum import Enum

class TeamworkSoftwareFreshness(str, Enum):
    Unknown = "unknown",
    Latest = "latest",
    UpdateAvailable = "updateAvailable",
    UnknownFutureValue = "unknownFutureValue",

