from enum import Enum

class WindowsUpdateCveSeverityLevel(str, Enum):
    # Severity of Critical
    Critical = "critical",
    # Severity of Important
    Important = "important",
    # Severity of Moderate
    Moderate = "moderate",
    # Reserved value of UnknownFutureValue
    UnknownFutureValue = "unknownFutureValue",

