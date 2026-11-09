from enum import Enum

class CustomFieldRollupType(str, Enum):
    NoRollup = "noRollup",
    Max = "max",
    Min = "min",
    Sum = "sum",
    Average = "average",
    UnknownFutureValue = "unknownFutureValue",

