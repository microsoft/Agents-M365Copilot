from enum import Enum

class SectionItemType(str, Enum):
    Chat = "chat",
    Channel = "channel",
    Meeting = "meeting",
    Community = "community",
    UnknownFutureValue = "unknownFutureValue",

