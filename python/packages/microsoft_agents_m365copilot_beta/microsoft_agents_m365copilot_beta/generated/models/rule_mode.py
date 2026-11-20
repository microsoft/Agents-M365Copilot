from enum import Enum

class RuleMode(str, Enum):
    Audit = "audit",
    AuditAndNotify = "auditAndNotify",
    Enforce = "enforce",
    PendingDeletion = "pendingDeletion",
    Test = "test",

