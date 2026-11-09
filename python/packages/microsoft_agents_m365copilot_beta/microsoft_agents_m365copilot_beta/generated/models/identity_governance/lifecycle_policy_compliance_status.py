from enum import Enum

class LifecyclePolicyComplianceStatus(str, Enum):
    NotEvaluated = "notEvaluated",
    Compliant = "compliant",
    NonCompliant = "nonCompliant",
    UnknownFutureValue = "unknownFutureValue",

