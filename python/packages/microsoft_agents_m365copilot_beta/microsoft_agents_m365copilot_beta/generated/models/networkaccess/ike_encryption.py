from enum import Enum

class IkeEncryption(str, Enum):
    Aes128 = "aes128",
    Aes192 = "aes192",
    Aes256 = "aes256",
    GcmAes128 = "gcmAes128",
    GcmAes256 = "gcmAes256",
    UnknownFutureValue = "unknownFutureValue",

