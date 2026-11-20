from enum import Enum

class PlannerChatMessageType(str, Enum):
    RichTextHtml = "richTextHtml",
    PlainText = "plainText",
    UnknownFutureValue = "unknownFutureValue",

