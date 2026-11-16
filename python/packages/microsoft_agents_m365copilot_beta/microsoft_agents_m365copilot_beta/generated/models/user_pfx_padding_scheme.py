from enum import Enum

class UserPfxPaddingScheme(str, Enum):
    # Unknown padding Scheme.
    None_ = "none",
    # Pkcs1 is no longer supported
    Pkcs1 = "pkcs1",
    # OaepSha1 is no longer supported
    OaepSha1 = "oaepSha1",
    # Use OAEP SHA-256 padding.
    OaepSha256 = "oaepSha256",
    # Use OAEP SHA-384 padding.
    OaepSha384 = "oaepSha384",
    # Use OAEP SHA-512 padding.
    OaepSha512 = "oaepSha512",

