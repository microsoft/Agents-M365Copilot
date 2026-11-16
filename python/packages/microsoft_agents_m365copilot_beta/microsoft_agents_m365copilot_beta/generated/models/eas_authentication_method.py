from enum import Enum

class EasAuthenticationMethod(str, Enum):
    # Authenticate with a username and password.
    UsernameAndPassword = "usernameAndPassword",
    # Authenticate with a certificate.
    Certificate = "certificate",
    # Authenticate with derived credential.
    DerivedCredential = "derivedCredential",

