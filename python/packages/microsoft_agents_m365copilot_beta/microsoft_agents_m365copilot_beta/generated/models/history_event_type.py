from enum import Enum

class HistoryEventType(str, Enum):
    Created = "created",
    Updated = "updated",
    Deleted = "deleted",
    Undeleted = "undeleted",
    Moved = "moved",
    UnknownFutureValue = "unknownFutureValue",

