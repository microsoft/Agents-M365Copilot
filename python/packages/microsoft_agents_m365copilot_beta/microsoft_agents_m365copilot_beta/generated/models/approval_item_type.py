from enum import Enum

class ApprovalItemType(str, Enum):
    Basic = "basic",
    BasicAwaitAll = "basicAwaitAll",
    Custom = "custom",
    CustomAwaitAll = "customAwaitAll",
    UnknownFutureValue = "unknownFutureValue",

