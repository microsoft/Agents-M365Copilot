from enum import Enum

class AccessReviewTimeoutBehavior(str, Enum):
    KeepAccess = "keepAccess",
    RemoveAccess = "removeAccess",
    AcceptAccessRecommendation = "acceptAccessRecommendation",
    UnknownFutureValue = "unknownFutureValue",

