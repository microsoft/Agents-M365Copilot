from enum import Enum

class CopilotConversationAttributionSource(str, Enum):
    Grounding = "grounding",
    Model = "model",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

