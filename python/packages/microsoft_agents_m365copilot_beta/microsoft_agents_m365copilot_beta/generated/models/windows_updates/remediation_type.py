from enum import Enum

class RemediationType(str, Enum):
    InPlaceUpgrade = "inPlaceUpgrade",
    UnknownFutureValue = "unknownFutureValue",

