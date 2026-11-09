from enum import Enum

class Windows10VpnProfileTarget(str, Enum):
    # User targeted VPN profile.
    User = "user",
    # Device targeted VPN profile.
    Device = "device",
    # AutoPilot Device targeted VPN profile.
    AutoPilotDevice = "autoPilotDevice",

