from enum import Enum

class PlannerTaskTargetKind(str, Enum):
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

