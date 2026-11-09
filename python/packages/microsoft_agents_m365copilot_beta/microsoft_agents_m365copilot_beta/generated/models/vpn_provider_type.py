from enum import Enum

class VpnProviderType(str, Enum):
    # Tunnel traffic is not explicitly configured.
    NotConfigured = "notConfigured",
    # Tunnel traffic at the application layer.
    AppProxy = "appProxy",
    # Tunnel traffic at the IP layer.
    PacketTunnel = "packetTunnel",

