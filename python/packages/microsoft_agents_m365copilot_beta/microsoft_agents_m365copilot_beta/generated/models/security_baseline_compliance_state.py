from enum import Enum

class SecurityBaselineComplianceState(str, Enum):
    # Unknown state
    Unknown = "unknown",
    # Secure state
    Secure = "secure",
    # Not applicable state
    NotApplicable = "notApplicable",
    # Not secure state
    NotSecure = "notSecure",
    # Error state
    Error = "error",
    # Conflict state
    Conflict = "conflict",

