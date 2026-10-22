from enum import Enum

class WindowsDefenderTamperProtectionOptions(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Enable windows defender tamper protection
    Enable = "enable",
    # Disable windows defender tamper protection
    Disable = "disable",

