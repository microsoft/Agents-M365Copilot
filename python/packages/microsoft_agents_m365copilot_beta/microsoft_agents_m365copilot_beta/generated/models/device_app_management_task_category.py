from enum import Enum

class DeviceAppManagementTaskCategory(str, Enum):
    # Unknown source.
    Unknown = "unknown",
    # Windows Defender ATP Threat & Vulnerability Management.
    AdvancedThreatProtection = "advancedThreatProtection",

