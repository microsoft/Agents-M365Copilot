from enum import Enum

class WiFiAuthenticationMethod(str, Enum):
    # Use an identity certificate for authentication.
    Certificate = "certificate",
    # Use username and password for authentication.
    UsernameAndPassword = "usernameAndPassword",
    # Use Derived Credential for authentication.
    DerivedCredential = "derivedCredential",

