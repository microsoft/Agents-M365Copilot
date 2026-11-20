from enum import Enum

class NetworkType(str, Enum):
    Intranet = "intranet",
    Extranet = "extranet",
    NamedNetwork = "namedNetwork",
    Trusted = "trusted",
    TrustedNamedLocation = "trustedNamedLocation",
    UnknownFutureValue = "unknownFutureValue",

