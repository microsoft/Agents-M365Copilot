from enum import Enum

class QualityUpdateCadence(str, Enum):
    Monthly = "monthly",
    OutOfBand = "outOfBand",
    UnknownFutureValue = "unknownFutureValue",

