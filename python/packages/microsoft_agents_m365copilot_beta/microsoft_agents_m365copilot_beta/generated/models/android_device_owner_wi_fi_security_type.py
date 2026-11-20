from enum import Enum

class AndroidDeviceOwnerWiFiSecurityType(str, Enum):
    # Open (No Authentication).
    Open = "open",
    # WEP Encryption.
    Wep = "wep",
    # WPA-Personal/WPA2-Personal.
    WpaPersonal = "wpaPersonal",
    # WPA-Enterprise/WPA2-Enterprise. Must use AndroidDeviceOwnerEnterpriseWifiConfiguration type to configure enterprise options.
    WpaEnterprise = "wpaEnterprise",

