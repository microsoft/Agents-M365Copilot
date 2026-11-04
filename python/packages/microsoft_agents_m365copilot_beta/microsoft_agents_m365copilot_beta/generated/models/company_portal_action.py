from enum import Enum

class CompanyPortalAction(str, Enum):
    # Unknown device action
    Unknown = "unknown",
    # Remove device from Company Portal
    Remove = "remove",
    # Reset device enrolled in Company Portal
    Reset = "reset",

