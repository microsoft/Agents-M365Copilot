from enum import Enum

class DeviceLicensingStatus(str, Enum):
    # Default. Set to unknown when status cannot be determined.
    Unknown = "unknown",
    # This status is set when the license refresh is started.
    LicenseRefreshStarted = "licenseRefreshStarted",
    # This status is set when the license refresh is pending.
    LicenseRefreshPending = "licenseRefreshPending",
    # This status is set when the device is not joined to Azure Active Directory.
    DeviceIsNotAzureActiveDirectoryJoined = "deviceIsNotAzureActiveDirectoryJoined",
    # This status is set when the Microsoft device identity is being verified.
    VerifyingMicrosoftDeviceIdentity = "verifyingMicrosoftDeviceIdentity",
    # This status is set when the Microsoft device identity verification fails.
    DeviceIdentityVerificationFailed = "deviceIdentityVerificationFailed",
    # This status is set when the Microsoft account identity is being verified.
    VerifyingMicrosoftAccountIdentity = "verifyingMicrosoftAccountIdentity",
    # This status is set when the Microsoft account identity verification fails.
    MicrosoftAccountVerificationFailed = "microsoftAccountVerificationFailed",
    # This status is set when the device license is being acquired.
    AcquiringDeviceLicense = "acquiringDeviceLicense",
    # This status is set when the device license is being refreshed.
    RefreshingDeviceLicense = "refreshingDeviceLicense",
    # This status is set when the device license refresh succeeds.
    DeviceLicenseRefreshSucceed = "deviceLicenseRefreshSucceed",
    # This status is set when the device license refresh fails.
    DeviceLicenseRefreshFailed = "deviceLicenseRefreshFailed",
    # This status is set when the device license is being removed.
    RemovingDeviceLicense = "removingDeviceLicense",
    # This status is set when the device license removing succeeds.
    DeviceLicenseRemoveSucceed = "deviceLicenseRemoveSucceed",
    # This status is set when the device license removing fails.
    DeviceLicenseRemoveFailed = "deviceLicenseRemoveFailed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

