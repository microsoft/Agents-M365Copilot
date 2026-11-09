from enum import Enum

class AuthenticationAppEvaluation(str, Enum):
    Success = "success",
    Failure = "failure",
    UnknownFutureValue = "unknownFutureValue",

