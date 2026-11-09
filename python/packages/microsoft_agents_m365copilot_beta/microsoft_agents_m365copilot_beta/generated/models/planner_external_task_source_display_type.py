from enum import Enum

class PlannerExternalTaskSourceDisplayType(str, Enum):
    None_ = "none",
    Default = "default",
    UnknownFutureValue = "unknownFutureValue",

