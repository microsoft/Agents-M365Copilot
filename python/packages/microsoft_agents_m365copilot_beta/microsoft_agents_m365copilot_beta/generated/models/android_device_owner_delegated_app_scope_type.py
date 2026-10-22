from enum import Enum

class AndroidDeviceOwnerDelegatedAppScopeType(str, Enum):
    # Unspecified; this value defaults to DELEGATED_SCOPE_UNSPECIFIED.
    Unspecified = "unspecified",
    # Specifies that the admin has given app permission to install and manage certificates on device.
    CertificateInstall = "certificateInstall",
    # Specifies that the admin has given app permission to capture network activity logs on device. More info on Network activity logs: https://developer.android.com/work/dpc/logging 
    CaptureNetworkActivityLog = "captureNetworkActivityLog",
    # Specified that the admin has given permission to capture security logs on device. More info on Security logs: https://developer.android.com/work/dpc/security#log_enterprise_device_activity
    CaptureSecurityLog = "captureSecurityLog",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

