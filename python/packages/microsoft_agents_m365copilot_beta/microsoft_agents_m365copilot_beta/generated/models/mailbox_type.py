from enum import Enum

class MailboxType(str, Enum):
    Unknown = "unknown",
    User = "user",
    Shared = "shared",
    UnknownFutureValue = "unknownFutureValue",

