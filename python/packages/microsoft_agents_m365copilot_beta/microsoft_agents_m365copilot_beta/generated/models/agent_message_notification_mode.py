from enum import Enum

class AgentMessageNotificationMode(str, Enum):
    AtMentionedMessagesOnly = "atMentionedMessagesOnly",
    AllMessages = "allMessages",
    UnknownFutureValue = "unknownFutureValue",

