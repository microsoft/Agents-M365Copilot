from enum import Enum

class DataCollectionStatus(str, Enum):
    Online = "online",
    Offline = "offline",
    UnknownFutureValue = "unknownFutureValue",

