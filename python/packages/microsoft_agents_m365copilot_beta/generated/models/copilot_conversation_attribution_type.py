from enum import Enum

class CopilotConversationAttributionType(str, Enum):
    Citation = "citation",
    Annotation = "annotation",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

