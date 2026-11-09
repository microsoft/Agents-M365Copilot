from enum import Enum

class PlannerTaskChatMentionType(str, Enum):
    User = "user",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

