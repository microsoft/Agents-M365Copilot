from enum import Enum

class IdentitySourceType(str, Enum):
    AzureActiveDirectory = "azureActiveDirectory",
    External = "external",
    UnknownFutureValue = "unknownFutureValue",

