from enum import Enum

class PlannerGoalStatus(str, Enum):
    NotStarted = "notStarted",
    OnTrack = "onTrack",
    Behind = "behind",
    AtRisk = "atRisk",
    Closed = "closed",
    UnknownFutureValue = "unknownFutureValue",

