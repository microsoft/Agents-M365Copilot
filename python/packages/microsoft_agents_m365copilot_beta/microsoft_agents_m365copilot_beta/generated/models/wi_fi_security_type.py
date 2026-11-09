from enum import Enum

class WiFiSecurityType(str, Enum):
    # Default. Indicates Wi-Fi security type is associated with Open (No Authentication).
    Open = "open",
    # Indicates Wi-Fi security type is associated with WPA-Personal.
    WpaPersonal = "wpaPersonal",
    # Indicates Wi-Fi security type is associated with WPA-Enterprise. Must use IOSEnterpriseWifiConfiguration type to configure enterprise options.
    WpaEnterprise = "wpaEnterprise",
    # Indicates Wi-Fi security type is associated with WEP Encryption.
    Wep = "wep",
    # Indicates Wi-Fi security type is associated with WPA2-Personal.
    Wpa2Personal = "wpa2Personal",
    # Indicates Wi-Fi security type is associated with WPA2-Enterprise. Must use WindowsWifiEnterpriseEAPConfiguration type to configure enterprise options.
    Wpa2Enterprise = "wpa2Enterprise",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Indicates Wi-Fi security type is associated with WPA3-Personal. Provides stronger encryption using Simultaneous Authentication of Equals (SAE).
    Wpa3Personal = "wpa3Personal",

