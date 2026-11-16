from enum import Enum

class EndpointSecurityConfigurationApplicablePlatform(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # MacOS.
    MacOS = "macOS",
    # Windows 10 and later.
    Windows10AndLater = "windows10AndLater",
    # Windows 10 and Windows Server.
    Windows10AndWindowsServer = "windows10AndWindowsServer",

