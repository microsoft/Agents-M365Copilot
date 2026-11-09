from enum import Enum

class AppManagementAuditLogAuditResult(str, Enum):
    NotApplicable = "notApplicable",
    WouldHaveBeenAllowed = "wouldHaveBeenAllowed",
    WouldHaveBeenBlocked = "wouldHaveBeenBlocked",
    UnknownFutureValue = "unknownFutureValue",

