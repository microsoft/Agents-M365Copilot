from enum import Enum

class ProvenanceAssertionType(str, Enum):
    IdentityVerification = "identityVerification",
    DerivedFromCredential = "derivedFromCredential",
    ManualAttestation = "manualAttestation",
    UnknownFutureValue = "unknownFutureValue",

