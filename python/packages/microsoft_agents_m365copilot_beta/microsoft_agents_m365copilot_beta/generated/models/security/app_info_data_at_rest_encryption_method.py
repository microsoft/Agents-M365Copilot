from enum import Enum

class AppInfoDataAtRestEncryptionMethod(str, Enum):
    Aes = "aes",
    BitLocker = "bitLocker",
    Blowfish = "blowfish",
    Des3 = "des3",
    Des = "des",
    Rc4 = "rc4",
    RsA = "rsA",
    NotSupported = "notSupported",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

