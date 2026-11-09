from enum import Enum

class FileEntityIdentifier(str, Enum):
    Sha1 = "sha1",
    InitiatingProcessSHA1 = "initiatingProcessSHA1",
    Sha256 = "sha256",
    InitiatingProcessSHA256 = "initiatingProcessSHA256",
    UnknownFutureValue = "unknownFutureValue",

