from enum import Enum

class DeviceManagementConfigurationPlatforms(str, Enum):
    # Indicates the settings contained in this configuration don't have a platform set.
    None_ = "none",
    # Indicates that the settings contained in associated configuration applies to the Android operating system. 
    Android = "android",
    # Indicates that the settings contained in associated configuration applies to the iOS operating system.
    IOS = "iOS",
    # Indicates that the settings contained in associated configuration applies to the MacOS operating system.
    MacOS = "macOS",
    # Indicates that the settings contained in associated configuration applies to the Windows 10X operating system.
    Windows10X = "windows10X",
    # Indicates that the settings contained in associated configuration applies to the Windows 10 operating system.
    Windows10 = "windows10",
    # Indicates that the settings contained in associated configuration applies to the Linux operating system.
    Linux = "linux",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Indicates that the settings contained in associated configuration applies to the android operating system corporate owned devices.
    AndroidEnterprise = "androidEnterprise",
    # Indicates that the settings contained in associated configuration applies to the android open source operating system.
    Aosp = "aosp",
    # Indicates that the settings contained in associated configuration applies to visionOS platform.
    VisionOS = "visionOS",
    # Indicates that the settings contained in associated configuration applies to the tvOS platform.
    TvOS = "tvOS",

