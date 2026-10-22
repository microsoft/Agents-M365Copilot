from enum import Enum

class CloudCertificationAuthorityHashingAlgorithm(str, Enum):
    # Default. The hashing algorithm is unknown or invalid.
    Unknown = "unknown",
    # The hashing algorithm is SHA-256.
    Sha256 = "sha256",
    # The hashing algorithm is SHA-384.
    Sha384 = "sha384",
    # The hashing algorithm is SHA-512.
    Sha512 = "sha512",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

