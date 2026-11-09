from enum import Enum

class CloudFirewallAction(str, Enum):
    Allow = "allow",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

