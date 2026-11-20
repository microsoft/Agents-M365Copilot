from enum import Enum

class AppInfoEncryptionProtocol(str, Enum):
    Tls1_0 = "tls1_0",
    Tls1_1 = "tls1_1",
    Tls1_2 = "tls1_2",
    Tls1_3 = "tls1_3",
    NotApplicable = "notApplicable",
    NotSupported = "notSupported",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",
    Ssl3 = "ssl3",

