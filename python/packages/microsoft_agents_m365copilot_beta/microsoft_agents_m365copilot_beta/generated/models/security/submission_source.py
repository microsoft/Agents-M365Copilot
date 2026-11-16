from enum import Enum

class SubmissionSource(str, Enum):
    User = "user",
    Administrator = "administrator",
    UnknownFutureValue = "unknownFutureValue",

