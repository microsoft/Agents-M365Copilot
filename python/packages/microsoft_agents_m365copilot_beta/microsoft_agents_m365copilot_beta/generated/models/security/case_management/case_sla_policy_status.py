from enum import Enum

class CaseSlaPolicyStatus(str, Enum):
    Active = "active",
    AtRisk = "atRisk",
    Breached = "breached",
    Paused = "paused",
    CompletedMet = "completedMet",
    CompletedBreached = "completedBreached",
    UnknownFutureValue = "unknownFutureValue",

