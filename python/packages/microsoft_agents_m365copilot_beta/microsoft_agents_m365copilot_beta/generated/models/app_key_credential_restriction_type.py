from enum import Enum

class AppKeyCredentialRestrictionType(str, Enum):
    AsymmetricKeyLifetime = "asymmetricKeyLifetime",
    TrustedCertificateAuthority = "trustedCertificateAuthority",
    UnknownFutureValue = "unknownFutureValue",

