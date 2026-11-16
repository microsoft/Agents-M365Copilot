from enum import Enum

class WindowsFirewallRuleInterfaceTypes(str, Enum):
    # No flags set.
    NotConfigured = "notConfigured",
    # The Remote Access interface type.
    RemoteAccess = "remoteAccess",
    # The Wireless interface type.
    Wireless = "wireless",
    # The LAN interface type.
    Lan = "lan",

