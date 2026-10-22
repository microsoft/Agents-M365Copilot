from enum import Enum

class UserNewMessageRestriction(str, Enum):
    Everyone = "everyone",
    EveryoneExceptGuests = "everyoneExceptGuests",
    Moderators = "moderators",
    UnknownFutureValue = "unknownFutureValue",

