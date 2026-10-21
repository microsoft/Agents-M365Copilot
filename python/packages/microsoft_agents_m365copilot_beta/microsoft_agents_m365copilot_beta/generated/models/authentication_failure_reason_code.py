from enum import Enum

class AuthenticationFailureReasonCode(str, Enum):
    Incomplete = "incomplete",
    Denied = "denied",
    SystemFailure = "systemFailure",
    BadRequest = "badRequest",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",
    UserError = "userError",
    ConfigError = "configError",

