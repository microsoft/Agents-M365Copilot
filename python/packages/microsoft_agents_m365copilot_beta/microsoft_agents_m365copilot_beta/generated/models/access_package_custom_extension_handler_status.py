from enum import Enum

class AccessPackageCustomExtensionHandlerStatus(str, Enum):
    RequestSent = "requestSent",
    RequestReceived = "requestReceived",
    UnknownFutureValue = "unknownFutureValue",

