from enum import Enum

class CopilotConversationState(str, Enum):
    # The conversation is active and can accept requests to chat.
    Active = "active",
    # Copilot has disengaged from the conversation due to a RAI issue and will reject further requests to chat.
    DisengagedForRai = "disengagedForRai",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

