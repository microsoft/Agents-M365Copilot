from enum import Enum

class ComplianceState(str, Enum):
    Compliant = "compliant",
    Warning = "warning",
    WarningNotify = "warningNotify",
    NonCompliant = "nonCompliant",
    UnknownFutureValue = "unknownFutureValue",

