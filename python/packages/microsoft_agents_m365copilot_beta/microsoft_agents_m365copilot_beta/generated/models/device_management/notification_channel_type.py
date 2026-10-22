from enum import Enum

class NotificationChannelType(str, Enum):
    Portal = "portal",
    Email = "email",
    PhoneCall = "phoneCall",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

