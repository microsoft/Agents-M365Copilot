from enum import Enum

class VpnServiceExceptionAction(str, Enum):
    # Make all traffic from that service go through the VPN
    ForceTrafficViaVPN = "forceTrafficViaVPN",
    # Allow the service outside of the VPN
    AllowTrafficOutside = "allowTrafficOutside",
    # Drop all traffic from the service
    DropTraffic = "dropTraffic",

