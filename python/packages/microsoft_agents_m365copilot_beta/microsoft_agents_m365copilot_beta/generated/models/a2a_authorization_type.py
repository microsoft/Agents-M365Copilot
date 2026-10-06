from enum import Enum

class A2aAuthorizationType(str, Enum):
    None_ = "none",
    OAuthPluginVault = "oAuthPluginVault",
    ApiKeyPluginVault = "apiKeyPluginVault",
    DynamicClientRegistration = "dynamicClientRegistration",
    ConnectionVault = "connectionVault",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

