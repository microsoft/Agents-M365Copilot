from enum import Enum

class EnrollmentRestrictionPlatformType(str, Enum):
    # Indicates that the enrollment configuration applies to all platforms
    AllPlatforms = "allPlatforms",
    # Indicates that the enrollment configuration applies only to iOS/iPadOS devices
    Ios = "ios",
    # Indicates that the enrollment configuration applies only to Windows devices
    Windows = "windows",
    # Indicates that the enrollment configuration applies only to Windows Phone devices
    WindowsPhone = "windowsPhone",
    # Indicates that the enrollment configuration applies only to Android devices
    Android = "android",
    # Indicates that the enrollment configuration applies only to Android for Work devices
    AndroidForWork = "androidForWork",
    # Indicates that the enrollment configuration applies only to macOS devices
    Mac = "mac",
    # Indicates that the enrollment configuration applies only to Linux devices
    Linux = "linux",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

