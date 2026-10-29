from enum import Enum

class RoutingPolicy(str, Enum):
    None_ = "none",
    NoMissedCall = "noMissedCall",
    DisableForwardingExceptPhone = "disableForwardingExceptPhone",
    DisableForwarding = "disableForwarding",
    PreferSkypeForBusiness = "preferSkypeForBusiness",
    UnknownFutureValue = "unknownFutureValue",

