from enum import Enum

class RestoreTimeRange(str, Enum):
    Before = "before",
    After = "after",
    BeforeOrAfter = "beforeOrAfter",
    UnknownFutureValue = "unknownFutureValue",

