from enum import Enum

class CloudCertificationAuthorityStatus(str, Enum):
    # Default. Indicates certification authority has an unknown or invalid status.
    Unknown = "unknown",
    # Indicates certification authority is active and can issue certificates.
    Active = "active",
    # Indicates certification authority has been paused from issuing certificates. Paused certification authorities can be put back in an active status to continue issuing certificates.
    Paused = "paused",
    # Indicates certification authority has been revoked. This is a permanent state that cannot be changed.
    Revoked = "revoked",
    # Indicates certification authority certificate signing request has been created and can be downloaded for signing and then be uploaded.
    SigningPending = "signingPending",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Indicates certification authority has expired and cannot issue certificates until renewed and activated.
    Expired = "expired",

