from enum import Enum

class EmailEntityIdentifier(str, Enum):
    NetworkMessageId = "networkMessageId",
    RecipientEmailAddress = "recipientEmailAddress",
    UnknownFutureValue = "unknownFutureValue",

