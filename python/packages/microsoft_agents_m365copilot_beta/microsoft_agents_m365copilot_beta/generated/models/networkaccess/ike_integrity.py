from enum import Enum

class IkeIntegrity(str, Enum):
    Sha256 = "sha256",
    Sha384 = "sha384",
    GcmAes128 = "gcmAes128",
    GcmAes256 = "gcmAes256",
    UnknownFutureValue = "unknownFutureValue",

