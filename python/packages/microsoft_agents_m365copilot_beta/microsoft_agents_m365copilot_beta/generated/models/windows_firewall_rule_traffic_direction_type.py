from enum import Enum

class WindowsFirewallRuleTrafficDirectionType(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # The rule applies to outbound traffic.
    Out = "out",
    # The rule applies to inbound traffic.
    In_ = "in",

