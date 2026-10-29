from enum import Enum

class AospDeviceOwnerWiFiSecurityType(str, Enum):
    # Open (No Authentication).
    Open = "open",
    # WEP Encryption.
    Wep = "wep",
    # WPA-Personal/WPA2-Personal.
    WpaPersonal = "wpaPersonal",
    # WPA-Enterprise/WPA2-Enterprise. Must use AOSPDeviceOwnerEnterpriseWifiConfiguration type to configure enterprise options.
    WpaEnterprise = "wpaEnterprise",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

