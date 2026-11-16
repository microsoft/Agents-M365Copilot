from enum import Enum

class Windows10VpnConnectionType(str, Enum):
    # Pulse Secure.
    PulseSecure = "pulseSecure",
    # F5 Edge Client.
    F5EdgeClient = "f5EdgeClient",
    # Dell SonicWALL Mobile Connection.
    DellSonicWallMobileConnect = "dellSonicWallMobileConnect",
    # Check Point Capsule VPN.
    CheckPointCapsuleVpn = "checkPointCapsuleVpn",
    # Automatic.
    Automatic = "automatic",
    # IKEv2.
    IkEv2 = "ikEv2",
    # L2TP.
    L2tp = "l2tp",
    # PPTP.
    Pptp = "pptp",
    # Citrix.
    Citrix = "citrix",
    # Palo Alto Networks GlobalProtect.
    PaloAltoGlobalProtect = "paloAltoGlobalProtect",
    # Cisco AnyConnect
    CiscoAnyConnect = "ciscoAnyConnect",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Microsoft Tunnel connection type
    MicrosoftTunnel = "microsoftTunnel",

