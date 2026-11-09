from enum import Enum

class DeploymentStateValue(str, Enum):
    Scheduled = "scheduled",
    Offering = "offering",
    Paused = "paused",
    Faulted = "faulted",
    Archived = "archived",
    UnknownFutureValue = "unknownFutureValue",

