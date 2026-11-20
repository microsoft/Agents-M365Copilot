from enum import Enum

class HistoryEntityType(str, Enum):
    Task = "task",
    UnknownFutureValue = "unknownFutureValue",

