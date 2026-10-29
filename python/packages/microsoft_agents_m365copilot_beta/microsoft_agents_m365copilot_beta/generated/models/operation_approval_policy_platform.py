from enum import Enum

class OperationApprovalPolicyPlatform(str, Enum):
    # Default. Indicates that a policy platform is not required for a chosen policy type.
    NotApplicable = "notApplicable",
    # Indicates that the configured policy platform is for Android Device Administrator.
    AndroidDeviceAdministrator = "androidDeviceAdministrator",
    # Indicates that the configured policy platform is for Android Enterprise.
    AndroidEnterprise = "androidEnterprise",
    # Indicates that the configured policy platform is for iOS/iPadOS.
    IOSiPadOS = "iOSiPadOS",
    # Indicates that the configured policy platform is for macOS.
    MacOS = "macOS",
    # Indicates that the configured policy platform is for Windows 10 and later.
    Windows10AndLater = "windows10AndLater",
    # Indicates that the configured policy platform is for Windows 8.1 and later.
    Windows81AndLater = "windows81AndLater",
    # Indicates that the configured policy platform is for Windows 10X.
    Windows10X = "windows10X",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

