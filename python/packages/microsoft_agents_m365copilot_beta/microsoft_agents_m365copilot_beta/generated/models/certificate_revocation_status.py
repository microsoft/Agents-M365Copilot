from enum import Enum

class CertificateRevocationStatus(str, Enum):
    # Not revoked.
    None_ = "none",
    # Revocation pending.
    Pending = "pending",
    # Revocation command issued.
    Issued = "issued",
    # Revocation failed.
    Failed = "failed",
    # Revoked.
    Revoked = "revoked",

