from enum import Enum

class LabelKind(str, Enum):
    All = "all",
    Enumerated = "enumerated",
    UnknownFutureValue = "unknownFutureValue",

