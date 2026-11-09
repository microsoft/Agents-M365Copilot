from enum import Enum

class DeviceCleanupRulePlatformType(str, Enum):
    # Default. Indicates that clean up rule is associated with all managed device platform.
    All = "all",
    # Indicates that clean up rule is associated with Android open source project managed device platform.
    AndroidAOSP = "androidAOSP",
    # Indicates that clean up rule is associated with Android device administrator managed device platform.
    AndroidDeviceAdministrator = "androidDeviceAdministrator",
    # Indicates that clean up rule is associated with Android dedicated and fully managed and Corporate Owned Work Profile managed device platform.
    AndroidDedicatedAndFullyManagedCorporateOwnedWorkProfile = "androidDedicatedAndFullyManagedCorporateOwnedWorkProfile",
    # Indicates that clean up rule is associated with ChromeOS managed device platform.
    ChromeOS = "chromeOS",
    # Indicates that clean up rule is associated with Android personally owned work profile managed device platform.
    AndroidPersonallyOwnedWorkProfile = "androidPersonallyOwnedWorkProfile",
    # Indicates that clean up rule is associated with IOS managed device platform.
    Ios = "ios",
    # Indicates that clean up rule is associated with MacOS managed device platform.
    MacOS = "macOS",
    # Indicates that clean up rule is associated with Windows managed device platform.
    Windows = "windows",
    # Indicates that clean up rule is associated with Windows Holographic managed device platform.
    WindowsHolographic = "windowsHolographic",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Indicates that clean up rule is associated with visionOS managed device platform.
    VisionOS = "visionOS",
    # Indicates that clean up rule is associated with tvOS managed device platform.
    TvOS = "tvOS",

