from enum import Enum

class AuthenticationTransformConstant(str, Enum):
    # MD596
    Md5_96 = "md5_96",
    # SHA196
    Sha1_96 = "sha1_96",
    # SHA256128
    Sha_256_128 = "sha_256_128",
    # GCMAES128
    Aes128Gcm = "aes128Gcm",
    # GCMAES192
    Aes192Gcm = "aes192Gcm",
    # GCMAES256
    Aes256Gcm = "aes256Gcm",

