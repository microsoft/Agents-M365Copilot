from enum import Enum

class SafeguardCategory(str, Enum):
    LikelyIssues = "likelyIssues",
    UnknownFutureValue = "unknownFutureValue",

