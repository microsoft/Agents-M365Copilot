from enum import Enum

class DefenderProtectionType(str, Enum):
    # Device default value, no intent.
    UserDefined = "userDefined",
    # Block functionality.
    Enable = "enable",
    # Allow functionality but generate logs.
    AuditMode = "auditMode",
    # Warning message to end user with ability to bypass block from attack surface reduction rule.
    Warn = "warn",
    # Not configured.
    NotConfigured = "notConfigured",

