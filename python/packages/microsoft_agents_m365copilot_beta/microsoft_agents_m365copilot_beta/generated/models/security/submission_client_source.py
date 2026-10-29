from enum import Enum

class SubmissionClientSource(str, Enum):
    Microsoft = "microsoft",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

