from enum import Enum

class OnlineMeetingForwarders(str, Enum):
    Everyone = "everyone",
    Organizer = "organizer",
    UnknownFutureValue = "unknownFutureValue",

