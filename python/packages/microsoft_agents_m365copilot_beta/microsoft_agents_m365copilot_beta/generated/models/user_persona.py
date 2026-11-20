from enum import Enum

class UserPersona(str, Enum):
    Unknown = "unknown",
    ExternalMember = "externalMember",
    ExternalGuest = "externalGuest",
    InternalMember = "internalMember",
    InternalGuest = "internalGuest",
    UnknownFutureValue = "unknownFutureValue",

