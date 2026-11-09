from enum import Enum

class Windows10VpnAuthenticationMethod(str, Enum):
    # Authenticate with a certificate.
    Certificate = "certificate",
    # Use username and password for authentication.
    UsernameAndPassword = "usernameAndPassword",
    # Authentication method is specified in custom EAP XML.
    CustomEapXml = "customEapXml",
    # Use Derived Credential for authentication.
    DerivedCredential = "derivedCredential",

