from enum import Enum

class VpnIntegrityAlgorithmType(str, Enum):
    # SHA2-256
    Sha2_256 = "sha2_256",
    # SHA1-96
    Sha1_96 = "sha1_96",
    # SHA1-160
    Sha1_160 = "sha1_160",
    # SHA2-384
    Sha2_384 = "sha2_384",
    # SHA2-512
    Sha2_512 = "sha2_512",
    # MD5
    Md5 = "md5",

