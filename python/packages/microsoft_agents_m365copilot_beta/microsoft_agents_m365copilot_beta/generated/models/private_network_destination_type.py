from enum import Enum

class PrivateNetworkDestinationType(str, Enum):
    IpAddress = "ipAddress",
    IpRange = "ipRange",
    IpRangeCidr = "ipRangeCidr",
    Fqdn = "fqdn",
    DnsSuffix = "dnsSuffix",
    UnknownFutureValue = "unknownFutureValue",
    ServicePrincipalName = "servicePrincipalName",

