from enum import Enum

class UriUsageType(str, Enum):
    RedirectUri = "redirectUri",
    IdentifierUri = "identifierUri",
    LoginUrl = "loginUrl",
    LogoutUrl = "logoutUrl",
    UnknownFutureValue = "unknownFutureValue",

