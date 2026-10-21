from enum import Enum

class PlannerChatThreadType(str, Enum):
    Task = "task",
    Plan = "plan",
    UnknownFutureValue = "unknownFutureValue",

