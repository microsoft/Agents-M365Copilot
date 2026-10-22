from enum import Enum

class WiredNetworkAuthenticationMethod(str, Enum):
    # Use an identity certificate for authentication.
    Certificate = "certificate",
    # Use username and password for authentication.
    UsernameAndPassword = "usernameAndPassword",
    # Use Derived Credential for authentication.
    DerivedCredential = "derivedCredential",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

