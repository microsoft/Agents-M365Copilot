from enum import Enum

class Scenario(str, Enum):
    Unknown = "unknown",
    Mfa = "mfa",
    Devices = "devices",
    UnknownFutureValue = "unknownFutureValue",
    ConditionalAccess = "conditionalAccess",
    Saml = "saml",
    Gsa = "gsa",

