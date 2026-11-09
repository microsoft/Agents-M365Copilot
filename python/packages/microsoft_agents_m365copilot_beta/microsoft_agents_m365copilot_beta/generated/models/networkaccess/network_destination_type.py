from enum import Enum

class NetworkDestinationType(str, Enum):
    Url = "url",
    Fqdn = "fqdn",
    IpAddress = "ipAddress",
    IpRange = "ipRange",
    IpSubnet = "ipSubnet",
    WebCategory = "webCategory",
    UnknownFutureValue = "unknownFutureValue",

