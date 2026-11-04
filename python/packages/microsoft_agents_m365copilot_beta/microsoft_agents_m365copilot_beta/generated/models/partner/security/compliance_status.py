from enum import Enum

class ComplianceStatus(str, Enum):
    Compliant = "compliant",
    Noncomplaint = "noncomplaint",
    UnknownFutureValue = "unknownFutureValue",

