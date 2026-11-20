from enum import Enum

class ExternalAuthenticationType(str, Enum):
    Passthru = "passthru",
    AadPreAuthentication = "aadPreAuthentication",

