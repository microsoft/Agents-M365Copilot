from enum import Enum

class AppleUserInitiatedEnrollmentType(str, Enum):
    # Default value in case enum parsing fails
    Unknown = "unknown",
    # Device enrollment via the iOS Company Portal. The default user-initiated enrollment type, which does not segregate corporate and personal data. Supported on all Intune-supported iOS/iPadOS versions.
    Device = "device",
    # Profile-driven user enrollment via the iOS Company Portal. An enrollment type that segregates corportate and personal data. Supported on devices running iOS/iPadOS 13 and higher.
    User = "user",
    # Account-driven user enrollment. Users will enroll from the iOS Settings app without using the iOS Company Portal. This enrollment type segregates corporate and personal data. Supported on devices running iOS/iPadOS 15 and higher.
    AccountDrivenUserEnrollment = "accountDrivenUserEnrollment",
    # Device enrollment via the web. Users will enroll without using the iOS Company Portal. This enrollment type does not segregate corporate and personal data. Supported on all Intune-supported iOS/iPadOS versions.
    WebDeviceEnrollment = "webDeviceEnrollment",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

