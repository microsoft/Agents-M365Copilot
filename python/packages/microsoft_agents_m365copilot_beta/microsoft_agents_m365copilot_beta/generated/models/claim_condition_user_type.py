from enum import Enum

class ClaimConditionUserType(str, Enum):
    Any = "any",
    Members = "members",
    AllGuests = "allGuests",
    AadGuests = "aadGuests",
    ExternalGuests = "externalGuests",
    UnknownFutureValue = "unknownFutureValue",

