from enum import Enum

class TransformationExtractType(str, Enum):
    Prefix = "prefix",
    Suffix = "suffix",
    UnknownFutureValue = "unknownFutureValue",

