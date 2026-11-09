from enum import Enum

class UserPfxIntendedPurpose(str, Enum):
    # No roles/usages assigned.
    Unassigned = "unassigned",
    # Valid for S/MIME encryption.
    SmimeEncryption = "smimeEncryption",
    # Valid for S/MIME signing.
    SmimeSigning = "smimeSigning",
    # Valid for use in VPN.
    Vpn = "vpn",
    # Valid for use in WiFi.
    Wifi = "wifi",

