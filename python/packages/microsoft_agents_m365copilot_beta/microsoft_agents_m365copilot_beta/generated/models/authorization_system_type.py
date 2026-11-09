from enum import Enum

class AuthorizationSystemType(str, Enum):
    Azure = "azure",
    Gcp = "gcp",
    Aws = "aws",
    UnknownFutureValue = "unknownFutureValue",

