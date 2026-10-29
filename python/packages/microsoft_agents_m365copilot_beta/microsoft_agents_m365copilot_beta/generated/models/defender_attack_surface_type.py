from enum import Enum

class DefenderAttackSurfaceType(str, Enum):
    # Default, which disables attack surface reduction rule.
    UserDefined = "userDefined",
    # Enable the attack surface reduction rule.
    Block = "block",
    # Evaluate how the ASR rule would impact your organization if enabled. Does not change functionality but generate logs.
    AuditMode = "auditMode",
    # Warning message to end user with ability to bypass block from attack surface reduction rule.
    Warn = "warn",
    # Disable the attack surface reduction rule
    Disable = "disable",

