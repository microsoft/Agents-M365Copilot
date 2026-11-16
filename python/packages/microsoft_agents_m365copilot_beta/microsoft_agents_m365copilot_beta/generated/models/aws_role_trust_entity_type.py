from enum import Enum

class AwsRoleTrustEntityType(str, Enum):
    None_ = "none",
    Service = "service",
    Sso = "sso",
    CrossAccount = "crossAccount",
    WebIdentity = "webIdentity",
    UnknownFutureValue = "unknownFutureValue",

