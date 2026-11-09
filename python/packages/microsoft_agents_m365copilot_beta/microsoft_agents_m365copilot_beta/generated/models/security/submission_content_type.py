from enum import Enum

class SubmissionContentType(str, Enum):
    Email = "email",
    Url = "url",
    File = "file",
    App = "app",
    UnknownFutureValue = "unknownFutureValue",

