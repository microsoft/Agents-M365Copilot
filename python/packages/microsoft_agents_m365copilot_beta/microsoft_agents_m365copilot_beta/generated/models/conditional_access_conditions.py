from enum import Enum

class ConditionalAccessConditions(str, Enum):
    None_ = "none",
    Application = "application",
    Users = "users",
    DevicePlatform = "devicePlatform",
    Location = "location",
    ClientType = "clientType",
    SignInRisk = "signInRisk",
    UserRisk = "userRisk",
    Time = "time",
    DeviceState = "deviceState",
    Client = "client",
    IpAddressSeenByAzureAD = "ipAddressSeenByAzureAD",
    IpAddressSeenByResourceProvider = "ipAddressSeenByResourceProvider",
    UnknownFutureValue = "unknownFutureValue",
    ServicePrincipals = "servicePrincipals",
    ServicePrincipalRisk = "servicePrincipalRisk",
    AuthenticationFlows = "authenticationFlows",
    InsiderRisk = "insiderRisk",

