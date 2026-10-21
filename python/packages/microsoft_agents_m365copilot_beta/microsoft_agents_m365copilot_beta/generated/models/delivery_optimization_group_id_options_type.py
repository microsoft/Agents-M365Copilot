from enum import Enum

class DeliveryOptimizationGroupIdOptionsType(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Active Directory site.
    AdSite = "adSite",
    # Authenticated domain SID.
    AuthenticatedDomainSid = "authenticatedDomainSid",
    # DHCP user option.
    DhcpUserOption = "dhcpUserOption",
    # DNS suffix.
    DnsSuffix = "dnsSuffix",

