from enum import Enum

class CustomFieldValueType(str, Enum):
    Text = "text",
    Date = "date",
    UtcDateTime = "utcDateTime",
    Number = "number",
    Decimal = "decimal",
    Flag = "flag",
    SingleChoiceText = "singleChoiceText",
    MultipleChoiceText = "multipleChoiceText",
    UnknownFutureValue = "unknownFutureValue",

