from enum import Enum

class PluginAuthTypes(str, Enum):
    None_ = "none",
    Basic = "basic",
    APIKey = "aPIKey",
    OAuthAuthorizationCodeFlow = "oAuthAuthorizationCodeFlow",
    OAuthClientCredentialsFlow = "oAuthClientCredentialsFlow",
    Aad = "aad",
    ServiceHttp = "serviceHttp",
    AadDelegated = "aadDelegated",
    OAuthPasswordGrantFlow = "oAuthPasswordGrantFlow",
    UnknownFutureValue = "unknownFutureValue",

