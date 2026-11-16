from enum import Enum

class CloudFirewallProtocol(str, Enum):
    Tcp = "tcp",
    Udp = "udp",
    UnknownFutureValue = "unknownFutureValue",

