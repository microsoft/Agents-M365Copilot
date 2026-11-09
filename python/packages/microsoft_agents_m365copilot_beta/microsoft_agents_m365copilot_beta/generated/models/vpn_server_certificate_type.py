from enum import Enum

class VpnServerCertificateType(str, Enum):
    # RSA
    Rsa = "rsa",
    # ECDSA256
    Ecdsa256 = "ecdsa256",
    # ECDSA384
    Ecdsa384 = "ecdsa384",
    # ECDSA521
    Ecdsa521 = "ecdsa521",

