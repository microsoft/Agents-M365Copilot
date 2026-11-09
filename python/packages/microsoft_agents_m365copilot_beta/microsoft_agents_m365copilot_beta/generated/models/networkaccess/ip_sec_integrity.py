from enum import Enum

class IpSecIntegrity(str, Enum):
    GcmAes128 = "gcmAes128",
    GcmAes192 = "gcmAes192",
    GcmAes256 = "gcmAes256",
    Sha256 = "sha256",
    UnknownFutureValue = "unknownFutureValue",

