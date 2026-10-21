from enum import Enum

class SamlAttributeNameFormat(str, Enum):
    Unspecified = "unspecified",
    Uri = "uri",
    Basic = "basic",
    UnknownFutureValue = "unknownFutureValue",

