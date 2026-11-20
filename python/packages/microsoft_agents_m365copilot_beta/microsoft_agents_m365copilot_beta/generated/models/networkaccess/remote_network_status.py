from enum import Enum

class RemoteNetworkStatus(str, Enum):
    TunnelDisconnected = "tunnelDisconnected",
    TunnelConnected = "tunnelConnected",
    BgpDisconnected = "bgpDisconnected",
    BgpConnected = "bgpConnected",
    RemoteNetworkAlive = "remoteNetworkAlive",
    UnknownFutureValue = "unknownFutureValue",

