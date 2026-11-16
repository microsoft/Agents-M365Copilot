from enum import Enum

class CaseTaskCategory(str, Enum):
    Uncategorized = "uncategorized",
    Triage = "triage",
    Contain = "contain",
    Investigate = "investigate",
    Remediate = "remediate",
    Prevent = "prevent",
    UnknownFutureValue = "unknownFutureValue",

