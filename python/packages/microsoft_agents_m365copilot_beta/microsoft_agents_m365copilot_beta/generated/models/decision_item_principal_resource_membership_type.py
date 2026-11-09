from enum import Enum

class DecisionItemPrincipalResourceMembershipType(str, Enum):
    Direct = "direct",
    Indirect = "indirect",
    UnknownFutureValue = "unknownFutureValue",

