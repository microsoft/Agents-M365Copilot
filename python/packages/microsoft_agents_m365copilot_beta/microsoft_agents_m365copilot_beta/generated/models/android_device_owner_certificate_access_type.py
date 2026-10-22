from enum import Enum

class AndroidDeviceOwnerCertificateAccessType(str, Enum):
    # Require user approval for all apps
    UserApproval = "userApproval",
    # Pre-grant certificate access for specific apps (require user approval for other apps).
    SpecificApps = "specificApps",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

