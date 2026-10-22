from enum import Enum

class CloudCertificationAuthorityCertificateKeySize(str, Enum):
    # Default. Unknown or invalid value.
    Unknown = "unknown",
    # A certificate generated using RSA cryptography and a key size of 2048 bits.
    Rsa2048 = "rsa2048",
    # A certificate generated using RSA cryptography and a key size of 3072 bits.
    Rsa3072 = "rsa3072",
    # A certificate generated using RSA cryptography and a key size of 4096 bits.
    Rsa4096 = "rsa4096",
    # A certificate generated using Elliptic Curve cryptography and a key size of 256 bits.
    ECP256 = "eCP256",
    # A certificate generated using Elliptic Curve cryptography and a key size of 256 bits with a Koblitz curve.
    ECP256k = "eCP256k",
    # A certificate generated using Elliptic Curve cryptography and a key size of 384 bits.
    ECP384 = "eCP384",
    # A certificate generated using Elliptic Curve cryptography and a key size of 521 bits.
    ECP521 = "eCP521",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

