from enum import Enum

class SkillPreviewState(str, Enum):
    Ga = "ga",
    Public = "public",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

