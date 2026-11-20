from enum import Enum

class CloudCertificationAuthorityType(str, Enum):
    # Default. Unknown or invalid certification authority type.
    Unknown = "unknown",
    # Indicates root certification authority. Can be used as the parent of an issuing certification authority. Root Certification Authority cannot issue leaf certificates.
    RootCertificationAuthority = "rootCertificationAuthority",
    # Indicates issuing (subordinate) certification authority. Must have a parent root certification authority. Issuing Certification Authority can issue leaf certificates.
    IssuingCertificationAuthority = "issuingCertificationAuthority",
    # Indicates issuing (subordinate) certification authority that has an external root certification authority. Issuing Certification Authority with external root can issue leaf certificates.
    IssuingCertificationAuthorityWithExternalRoot = "issuingCertificationAuthorityWithExternalRoot",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

