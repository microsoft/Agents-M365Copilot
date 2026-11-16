from enum import Enum

class VppTokenActionFailureReason(str, Enum):
    # None.
    None_ = "none",
    # There was an error on Apple's service.
    AppleFailure = "appleFailure",
    # There was an internal error.
    InternalError = "internalError",
    # There was an error because the Apple Volume Purchase Program token was expired.
    ExpiredVppToken = "expiredVppToken",
    # There was an error because the Apple Volume Purchase Program Push Notification certificate expired.
    ExpiredApplePushNotificationCertificate = "expiredApplePushNotificationCertificate",

