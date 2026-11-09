from enum import Enum

class OnlineMeetingRole(str, Enum):
    Attendee = "attendee",
    Presenter = "presenter",
    Producer = "producer",
    UnknownFutureValue = "unknownFutureValue",
    Coorganizer = "coorganizer",

