from enum import Enum

class CreditRequestType(str, Enum):
    # The request type is not known.
    Unknown = "unknown",
    # The requester has no credits and is requesting their first allocation.
    FirstTimeAccess = "firstTimeAccess",
    # The requester has already used credits and needs more because they have run out or are about to.
    AdditionalCredits = "additionalCredits",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

