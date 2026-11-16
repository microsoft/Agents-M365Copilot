from enum import Enum

class IpSecEncryption(str, Enum):
    None_ = "none",
    GcmAes128 = "gcmAes128",
    GcmAes192 = "gcmAes192",
    GcmAes256 = "gcmAes256",
    UnknownFutureValue = "unknownFutureValue",

