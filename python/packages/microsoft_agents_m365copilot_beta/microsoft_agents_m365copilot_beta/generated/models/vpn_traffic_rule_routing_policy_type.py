from enum import Enum

class VpnTrafficRuleRoutingPolicyType(str, Enum):
    # No routing policy specified.
    None_ = "none",
    # Network traffic for the specified app will be routed through the VPN.
    SplitTunnel = "splitTunnel",
    # All network traffic will be routed through the VPN.
    ForceTunnel = "forceTunnel",

