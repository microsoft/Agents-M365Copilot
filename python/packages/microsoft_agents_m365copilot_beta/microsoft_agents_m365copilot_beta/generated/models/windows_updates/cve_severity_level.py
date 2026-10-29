from enum import Enum

class CveSeverityLevel(str, Enum):
    Critical = "critical",
    Important = "important",
    Moderate = "moderate",
    UnknownFutureValue = "unknownFutureValue",

