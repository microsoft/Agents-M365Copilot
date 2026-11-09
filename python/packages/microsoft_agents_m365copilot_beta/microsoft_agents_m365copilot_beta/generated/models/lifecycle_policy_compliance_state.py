from enum import Enum

class LifecyclePolicyComplianceState(str, Enum):
    Compliant = "compliant",
    Warning = "warning",
    WarningNotify = "warningNotify",
    NonCompliant = "nonCompliant",

