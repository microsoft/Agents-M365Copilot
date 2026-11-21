from enum import Enum

class ChainBreakReason(str, Enum):
    None_ = "none",
    IdvRevoked = "idvRevoked",
    SourceCredentialRevoked = "sourceCredentialRevoked",
    UnknownFutureValue = "unknownFutureValue",

