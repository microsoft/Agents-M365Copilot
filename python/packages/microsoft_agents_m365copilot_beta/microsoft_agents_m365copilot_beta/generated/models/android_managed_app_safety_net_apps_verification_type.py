from enum import Enum

class AndroidManagedAppSafetyNetAppsVerificationType(str, Enum):
    # no requirement set
    None_ = "none",
    # require that Android device has SafetyNet Apps Verification enabled
    Enabled = "enabled",

