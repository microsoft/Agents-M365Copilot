from enum import Enum

class ChainState(str, Enum):
    Intact = "intact",
    Broken = "broken",
    UnknownFutureValue = "unknownFutureValue",

