from enum import Enum

class ReplyRestriction(str, Enum):
    Everyone = "everyone",
    AuthorAndModerators = "authorAndModerators",
    UnknownFutureValue = "unknownFutureValue",

