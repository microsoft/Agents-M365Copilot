from enum import Enum

class TokenFormat(str, Enum):
    Saml = "saml",
    Jwt = "jwt",
    UnknownFutureValue = "unknownFutureValue",

