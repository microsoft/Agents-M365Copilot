from enum import Enum

class NotificationDestination(str, Enum):
    None_ = "none",
    Api = "api",
    Email = "email",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

