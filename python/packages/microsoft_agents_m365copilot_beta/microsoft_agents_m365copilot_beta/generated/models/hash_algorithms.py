from enum import Enum

class HashAlgorithms(str, Enum):
    # SHA-1 Hash Algorithm.
    Sha1 = "sha1",
    # SHA-2 Hash Algorithm.
    Sha2 = "sha2",

