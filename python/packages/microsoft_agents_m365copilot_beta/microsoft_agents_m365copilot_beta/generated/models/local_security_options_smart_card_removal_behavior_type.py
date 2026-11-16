from enum import Enum

class LocalSecurityOptionsSmartCardRemovalBehaviorType(str, Enum):
    # No Action
    NoAction = "noAction",
    # Lock Workstation
    LockWorkstation = "lockWorkstation",
    # Force Logoff
    ForceLogoff = "forceLogoff",
    # Disconnect if a remote Remote Desktop Services session
    DisconnectRemoteDesktopSession = "disconnectRemoteDesktopSession",

