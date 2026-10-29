from enum import Enum

class ThreatIntelligenceAction(str, Enum):
    Allow = "allow",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

