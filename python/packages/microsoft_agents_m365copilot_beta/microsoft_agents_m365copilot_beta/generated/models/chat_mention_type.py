from enum import Enum

class ChatMentionType(str, Enum):
    User = "user",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

