from enum import Enum

class AzureRoleDefinitionType(str, Enum):
    System = "system",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

