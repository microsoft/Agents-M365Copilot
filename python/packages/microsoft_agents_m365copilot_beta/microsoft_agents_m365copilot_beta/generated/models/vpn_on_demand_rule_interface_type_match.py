from enum import Enum

class VpnOnDemandRuleInterfaceTypeMatch(str, Enum):
    # NotConfigured
    NotConfigured = "notConfigured",
    # Ethernet.
    Ethernet = "ethernet",
    # WiFi.
    WiFi = "wiFi",
    # Cellular.
    Cellular = "cellular",

