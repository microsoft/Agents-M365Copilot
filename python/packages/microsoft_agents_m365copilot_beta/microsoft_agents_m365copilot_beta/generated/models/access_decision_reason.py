from enum import Enum

class AccessDecisionReason(str, Enum):
    # The user is allowed to consume.
    Allowed = "allowed",
    # The user is not entitled to the service.
    NotEntitled = "notEntitled",
    # The applicable limit is exhausted.
    LimitExhausted = "limitExhausted",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

