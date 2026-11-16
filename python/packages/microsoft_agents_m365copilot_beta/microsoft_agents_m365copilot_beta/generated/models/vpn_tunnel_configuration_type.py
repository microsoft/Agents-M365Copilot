from enum import Enum

class VpnTunnelConfigurationType(str, Enum):
    # WiFi and Cellular Tunnels
    WifiAndCellular = "wifiAndCellular",
    # Cellular Tunnel Only
    Cellular = "cellular",
    # WiFi Tunnel Only
    Wifi = "wifi",

