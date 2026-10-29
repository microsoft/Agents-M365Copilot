from enum import Enum

class PrintDuplexConfiguration(str, Enum):
    TwoSidedLongEdge = "twoSidedLongEdge",
    TwoSidedShortEdge = "twoSidedShortEdge",
    OneSided = "oneSided",

