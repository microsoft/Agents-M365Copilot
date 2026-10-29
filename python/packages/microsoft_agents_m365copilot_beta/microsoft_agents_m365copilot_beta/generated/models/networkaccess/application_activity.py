from enum import Enum

class ApplicationActivity(str, Enum):
    None_ = "none",
    Prompt = "prompt",
    Mcp = "mcp",
    UnknownFutureValue = "unknownFutureValue",

