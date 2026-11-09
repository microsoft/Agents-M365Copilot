from enum import Enum

class PluginCategory(str, Enum):
    Hidden = "hidden",
    Microsoft = "microsoft",
    MicrosoftConnectors = "microsoftConnectors",
    Other = "other",
    Web = "web",
    Testing = "testing",
    Plugin = "plugin",
    UnknownFutureValue = "unknownFutureValue",

