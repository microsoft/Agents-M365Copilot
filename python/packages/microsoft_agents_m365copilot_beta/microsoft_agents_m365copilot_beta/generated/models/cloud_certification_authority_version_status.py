from enum import Enum

class CloudCertificationAuthorityVersionStatus(str, Enum):
    # Default. Indicates certification authority version has an unknown or invalid status.
    Unknown = "unknown",
    # Indicates certification authority version is active and can issue leaf certificates.
    Active = "active",
    # Indicates certification authority version was created during the renewal process and is currently in the staged phase. Upon activation, it becomes the new active certification authority version.
    Staged = "staged",
    # Indicates certification authority version has been paused from issuing certificates. The paused state is supported only for active certification authority versions. Staged certification authority versions cannot be paused and may only be revoked.
    Paused = "paused",
    # Indicates certification authority version has been retired after renewal. The retired certification authority version is not expired and continues to validate certificates it previously issued.
    Retired = "retired",
    # Indicates certification authority version has exceeded its validity period.
    Expired = "expired",
    # Indicates certification authority version has been revoked. This is a permanent state that cannot be changed.
    Revoked = "revoked",
    # Indicates certification authority version has been decommissioned. Only applicable for staged certification authority versions. Decommissioned certification authority versions cannot issue or validate leaf certificates. This is a permanent state that cannot be changed.
    Decommissioned = "decommissioned",
    # Indicates certification authority version was created with a Bring Your Own CA (BYOCA) root and requires external signing.
    SigningPending = "signingPending",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

