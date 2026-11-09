from enum import Enum

class AndroidWiFiSecurityType(str, Enum):
    # Default. Indicates Android Wifi Security Type is set to "Open" i.e. no authentication is required. (No Authentication).
    Open = "open",
    # Indicates Android Wifi Security Type is set to WPA encryption. Must use AndroidWorkProfileEnterpriseWifiConfiguration type to configure enterprise options.
    WpaEnterprise = "wpaEnterprise",
    # Indicates Android Wifi Security Type is set to WPA2 encryption. Must use AndroidWorkProfileEnterpriseWifiConfiguration type to configure enterprise options.
    Wpa2Enterprise = "wpa2Enterprise",
    # Indicates Android Wifi Security Type is set to WEP encryption. This restricts the preSharedKey to a valid passphrase (5 or 13 characters) or a valid HEX key (10 or 26 hexidecimal characters). Use AndroidWorkProfileWifiConfiguration to configure basic Wi-Fi options.
    Wep = "wep",
    #  Indicates Android Wifi Security Type is set to WPA encryption. This restricts the preSharedKey to a string between 8 and 64 characters long. Use AndroidWorkProfileWifiConfiguration to configure basic Wi-Fi options.
    WpaPersonal = "wpaPersonal",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

