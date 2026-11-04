from enum import Enum

class MeetingRegistrantStatus(str, Enum):
    Registered = "registered",
    Canceled = "canceled",
    Processing = "processing",
    UnknownFutureValue = "unknownFutureValue",

