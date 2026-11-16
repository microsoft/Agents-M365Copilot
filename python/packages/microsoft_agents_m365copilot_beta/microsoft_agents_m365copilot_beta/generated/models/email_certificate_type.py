from enum import Enum

class EmailCertificateType(str, Enum):
    # Do not use a certificate as a source.
    None_ = "none",
    # Use an certificate for certificate source.
    Certificate = "certificate",
    # Use a derived credential for certificate source.
    DerivedCredential = "derivedCredential",

