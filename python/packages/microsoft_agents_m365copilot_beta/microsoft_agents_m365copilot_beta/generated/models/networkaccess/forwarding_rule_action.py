from enum import Enum

class ForwardingRuleAction(str, Enum):
    Bypass = "bypass",
    Forward = "forward",
    UnknownFutureValue = "unknownFutureValue",

