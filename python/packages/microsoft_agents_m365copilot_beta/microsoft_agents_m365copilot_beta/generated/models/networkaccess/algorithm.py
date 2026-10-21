from enum import Enum

class Algorithm(str, Enum):
    Md5 = "md5",
    Sha1 = "sha1",
    Sha256 = "sha256",
    Sha256ac = "sha256ac",
    UnknownFutureValue = "unknownFutureValue",

