from enum import Enum

class PlannerCreationSourceKind(str, Enum):
    None_ = "none",
    External = "external",
    Publication = "publication",
    UnknownFutureValue = "unknownFutureValue",

