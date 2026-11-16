from enum import Enum

class DeviceManagementConfigurationAppleApplicabilityConstraint(str, Enum):
    # Not supported.
    NotSupported = "notSupported",
    # Available on device channel.
    DeviceChannel = "deviceChannel",
    # Available on user channel.
    UserChannel = "userChannel",
    # Requires supervised devices.
    RequireSupervised = "requireSupervised",
    # Requires a DEP enrolled macOS device.
    RequireDepEnrolled = "requireDepEnrolled",
    # Requires user-approved enrolled macOS device.
    RequireUserApproved = "requireUserApproved",
    # Allowed for user enrolled devices.
    AllowUserEnrollment = "allowUserEnrollment",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

