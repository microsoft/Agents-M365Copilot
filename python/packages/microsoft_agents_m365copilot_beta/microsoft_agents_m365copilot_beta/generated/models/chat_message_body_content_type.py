from enum import Enum

class ChatMessageBodyContentType(str, Enum):
    Text = "text",
    Html = "html",
    Markdown = "markdown",
    UnknownFutureValue = "unknownFutureValue",

