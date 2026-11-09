from enum import Enum

class InformationBarrierMode(str, Enum):
    Open = "open",
    OwnerModerated = "ownerModerated",
    Explicit = "explicit",
    UnknownFutureValue = "unknownFutureValue",

