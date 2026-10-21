from enum import Enum

class TransformationTrimType(str, Enum):
    Leading = "leading",
    Trailing = "trailing",
    LeadingAndTrailing = "leadingAndTrailing",
    UnknownFutureValue = "unknownFutureValue",

