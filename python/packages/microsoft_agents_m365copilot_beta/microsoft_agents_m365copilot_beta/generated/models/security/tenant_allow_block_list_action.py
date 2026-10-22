from enum import Enum

class TenantAllowBlockListAction(str, Enum):
    Allow = "allow",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

