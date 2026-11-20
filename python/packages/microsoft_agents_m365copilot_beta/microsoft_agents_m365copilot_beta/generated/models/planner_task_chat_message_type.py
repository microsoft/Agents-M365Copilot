from enum import Enum

class PlannerTaskChatMessageType(str, Enum):
    RichTextHtml = "richTextHtml",
    PlainText = "plainText",
    UnknownFutureValue = "unknownFutureValue",

