from enum import Enum

class SignInAccessType(str, Enum):
    None_ = "none",
    B2bCollaboration = "b2bCollaboration",
    B2bDirectConnect = "b2bDirectConnect",
    MicrosoftSupport = "microsoftSupport",
    ServiceProvider = "serviceProvider",
    UnknownFutureValue = "unknownFutureValue",
    Passthrough = "passthrough",

