from enum import Enum

class PrivateNetworkProtocol(str, Enum):
    Tcp = "tcp",
    Udp = "udp",
    UnknownFutureValue = "unknownFutureValue",

