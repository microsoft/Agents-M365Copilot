from enum import Enum

class SectionSortType(str, Enum):
    MostRecent = "mostRecent",
    UnreadThenMostRecent = "unreadThenMostRecent",
    NameAlphabetical = "nameAlphabetical",
    UserDefinedCustomOrder = "userDefinedCustomOrder",
    UnknownFutureValue = "unknownFutureValue",

