from enum import Enum

class DiamondModel(str, Enum):
    Unknown = "unknown",
    Adversary = "adversary",
    Capability = "capability",
    Infrastructure = "infrastructure",
    Victim = "victim",
    UnknownFutureValue = "unknownFutureValue",

