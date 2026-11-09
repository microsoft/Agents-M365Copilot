from enum import Enum

class DeviceComplianceScriptPlatformType(str, Enum):
    # Default. Indicates that the compliance script targets devices running Windows 10 and later.
    Windows10 = "windows10",
    # Indicates that the compliance script targets devices running Linux.
    Linux = "linux",
    # Indicates that the compliance script targets devices running macOS.
    MacOS = "macOS",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

