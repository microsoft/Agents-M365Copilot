from enum import Enum

class AppleVpnConnectionType(str, Enum):
    # Cisco AnyConnect.
    CiscoAnyConnect = "ciscoAnyConnect",
    # Pulse Secure.
    PulseSecure = "pulseSecure",
    # F5 Edge Client.
    F5EdgeClient = "f5EdgeClient",
    # Dell SonicWALL Mobile Connection.
    DellSonicWallMobileConnect = "dellSonicWallMobileConnect",
    # Check Point Capsule VPN.
    CheckPointCapsuleVpn = "checkPointCapsuleVpn",
    # Custom VPN.
    CustomVpn = "customVpn",
    # Cisco (IPSec).
    CiscoIPSec = "ciscoIPSec",
    # Citrix.
    Citrix = "citrix",
    # Cisco AnyConnect V2.
    CiscoAnyConnectV2 = "ciscoAnyConnectV2",
    # Palo Alto Networks GlobalProtect.
    PaloAltoGlobalProtect = "paloAltoGlobalProtect",
    # Zscaler Private Access.
    ZscalerPrivateAccess = "zscalerPrivateAccess",
    # F5 Access 2018.
    F5Access2018 = "f5Access2018",
    # Citrix Sso.
    CitrixSso = "citrixSso",
    # Palo Alto Networks GlobalProtect V2.
    PaloAltoGlobalProtectV2 = "paloAltoGlobalProtectV2",
    # IKEv2.
    IkEv2 = "ikEv2",
    # AlwaysOn.
    AlwaysOn = "alwaysOn",
    # Microsoft Tunnel.
    MicrosoftTunnel = "microsoftTunnel",
    # NetMotion Mobility.
    NetMotionMobility = "netMotionMobility",
    # Microsoft Protect.
    MicrosoftProtect = "microsoftProtect",

