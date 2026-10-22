from enum import Enum

class RequestedDeploymentStateValue(str, Enum):
    None_ = "none",
    Paused = "paused",
    Archived = "archived",
    UnknownFutureValue = "unknownFutureValue",

