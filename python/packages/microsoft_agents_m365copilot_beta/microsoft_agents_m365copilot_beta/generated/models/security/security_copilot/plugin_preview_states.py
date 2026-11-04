from enum import Enum

class PluginPreviewStates(str, Enum):
    Ga = "ga",
    Public = "public",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

