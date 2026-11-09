from enum import Enum

class PromptType(str, Enum):
    Unknown = "unknown",
    Context = "context",
    Prompt = "prompt",
    Skill = "skill",
    Feedback = "feedback",
    UnknownFutureValue = "unknownFutureValue",

