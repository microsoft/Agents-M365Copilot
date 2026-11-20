from enum import Enum

class InvestigationOutputType(str, Enum):
    Summary = "summary",
    Artifact = "artifact",
    UnknownFutureValue = "unknownFutureValue",

