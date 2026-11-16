from enum import Enum

class EnrichmentState(str, Enum):
    None_ = "none",
    InProgress = "inProgress",
    Enriched = "enriched",
    UnknownFutureValue = "unknownFutureValue",

