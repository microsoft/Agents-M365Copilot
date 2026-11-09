from enum import Enum

class AndroidAppCredentialProviderRoleState(str, Enum):
    # Default. Indicates the app's ability to act as a credential provider has not been configured. When set to 'notConfigured', the Android OS will determine whether the app is allowed to act as a credential provider or not.
    NotConfigured = "notConfigured",
    # Indicates the app is allowed to act as a credential provider.
    Allowed = "allowed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

