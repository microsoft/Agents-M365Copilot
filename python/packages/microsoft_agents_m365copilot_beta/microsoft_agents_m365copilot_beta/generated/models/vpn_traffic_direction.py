from enum import Enum

class VpnTrafficDirection(str, Enum):
    # The rule applies to all outbound traffic.
    Outbound = "outbound",
    # The rule applies to all inbound traffic.
    Inbound = "inbound",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

