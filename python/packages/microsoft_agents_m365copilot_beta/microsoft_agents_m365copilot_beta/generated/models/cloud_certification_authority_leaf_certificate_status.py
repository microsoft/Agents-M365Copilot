from enum import Enum

class CloudCertificationAuthorityLeafCertificateStatus(str, Enum):
    # Default. Unknown or invalid status.
    Unknown = "unknown",
    # Certificate is active, indicating it is in its validity period and not revoked.
    Active = "active",
    # Certificate has been revoked by its issuing certification authority.
    Revoked = "revoked",
    # Certificate has expired.
    Expired = "expired",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

