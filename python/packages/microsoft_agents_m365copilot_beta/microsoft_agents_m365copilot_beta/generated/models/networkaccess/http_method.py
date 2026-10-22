from enum import Enum

class HttpMethod(str, Enum):
    Get = "get",
    Post = "post",
    Put = "put",
    Delete = "delete",
    Head = "head",
    Options = "options",
    Connect = "connect",
    Patch = "patch",
    Trace = "trace",
    UnknownFutureValue = "unknownFutureValue",

