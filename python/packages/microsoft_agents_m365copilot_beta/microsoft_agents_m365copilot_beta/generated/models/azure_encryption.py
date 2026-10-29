from enum import Enum

class AzureEncryption(str, Enum):
    MicrosoftStorage = "microsoftStorage",
    MicrosoftKeyVault = "microsoftKeyVault",
    Customer = "customer",
    UnknownFutureValue = "unknownFutureValue",

