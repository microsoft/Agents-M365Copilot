from enum import Enum

class Platform(str, Enum):
    # Default.Indicates the managed device is not known and is associated with 'Unknown' device platform.
    Unknown = "unknown",
    # Indicates the managed device is Apple device that runs on iOS operation system.
    Ios = "ios",
    # Indicates the managed device is a Android device that runs on Android operation system. 
    Android = "android",
    # Indicates the managed device is a Windows device that runs on Windows operation system.
    Windows = "windows",
    # Indicates the managed device is a Windows-based mobile device that runs on Windows Mobile operation system.
    WindowsMobile = "windowsMobile",
    # Indicates the managed device is Apple device that runs on MacOS operation system.
    MacOS = "macOS",
    # Indicates the managed device is Apple device that runs on VisionOS operation system.
    VisionOS = "visionOS",
    # Indicates the managed device is Apple device that runs on tvOS operation system.
    TvOS = "tvOS",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

