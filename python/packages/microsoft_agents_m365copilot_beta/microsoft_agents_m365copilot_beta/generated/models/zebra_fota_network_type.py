from enum import Enum

class ZebraFotaNetworkType(str, Enum):
    # The device will install the update regardless of current network type.
    Any = "any",
    # The device will install the update only when connected to WiFi network.
    Wifi = "wifi",
    # The device will install the update only when connected a Cellular network.
    Cellular = "cellular",
    # The device will install the update when connected both WiFi and Cellular.
    WifiAndCellular = "wifiAndCellular",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

