from enum import Enum

class QualityUpdateClassification(str, Enum):
    All = "all",
    Security = "security",
    NonSecurity = "nonSecurity",
    UnknownFutureValue = "unknownFutureValue",

