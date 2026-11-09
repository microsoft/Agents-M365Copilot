from enum import Enum

class AlertType(str, Enum):
    Unknown = "unknown",
    MfaSignInFailure = "mfaSignInFailure",
    ManagedDeviceSignInFailure = "managedDeviceSignInFailure",
    CompliantDeviceSignInFailure = "compliantDeviceSignInFailure",
    UnknownFutureValue = "unknownFutureValue",
    ConditionalAccessBlockedSignIn = "conditionalAccessBlockedSignIn",
    SamlSignInFailure = "samlSignInFailure",
    InternetAppBlockedByPolicy = "internetAppBlockedByPolicy",
    PrivateAppBlockedByConnector = "privateAppBlockedByConnector",
    RemoteNetworkTunnelConnectivity = "remoteNetworkTunnelConnectivity",
    RemoteNetworkBgpConnectivity = "remoteNetworkBgpConnectivity",

