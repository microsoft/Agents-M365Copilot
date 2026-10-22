from enum import Enum

class ContentLinkType(str, Enum):
    DocumentReference = "documentReference",
    WebReference = "webReference",
    UnknownFutureValue = "unknownFutureValue",

