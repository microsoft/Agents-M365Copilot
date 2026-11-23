from enum import Enum

class InvestigationMessageRole(str, Enum):
    User = "user",
    Agent = "agent",
    System = "system",
    Tool = "tool",
    UnknownFutureValue = "unknownFutureValue",

