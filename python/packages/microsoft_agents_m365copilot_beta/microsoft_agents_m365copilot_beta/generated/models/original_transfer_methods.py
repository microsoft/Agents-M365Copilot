from enum import Enum

class OriginalTransferMethods(str, Enum):
    None_ = "none",
    DeviceCodeFlow = "deviceCodeFlow",
    AuthenticationTransfer = "authenticationTransfer",
    UnknownFutureValue = "unknownFutureValue",

