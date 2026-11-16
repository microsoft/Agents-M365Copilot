from enum import Enum

class PluginSettingType(str, Enum):
    String = "string",
    Bool = "bool",
    Array = "array",
    Enum = "enum",
    SecretString = "secretString",
    UnknownFutureValue = "unknownFutureValue",

