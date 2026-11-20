from enum import Enum

class VpnAuthenticationMethod(str, Enum):
    # Authenticate with a certificate.
    Certificate = "certificate",
    # Use username and password for authentication.
    UsernameAndPassword = "usernameAndPassword",
    # Use Shared Secret for Authentication.  Only valid for iOS IKEv2.
    SharedSecret = "sharedSecret",
    # Use Derived Credential for Authentication.
    DerivedCredential = "derivedCredential",
    # Use Azure AD for authentication.
    AzureAD = "azureAD",

