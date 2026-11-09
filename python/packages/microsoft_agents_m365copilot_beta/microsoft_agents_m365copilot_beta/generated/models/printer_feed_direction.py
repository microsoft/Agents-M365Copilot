from enum import Enum

class PrinterFeedDirection(str, Enum):
    LongEdgeFirst = "longEdgeFirst",
    ShortEdgeFirst = "shortEdgeFirst",

