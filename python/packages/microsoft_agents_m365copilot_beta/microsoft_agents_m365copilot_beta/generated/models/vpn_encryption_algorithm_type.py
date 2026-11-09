from enum import Enum

class VpnEncryptionAlgorithmType(str, Enum):
    # AES-256
    Aes256 = "aes256",
    # DES
    Des = "des",
    # 3DES
    TripleDes = "tripleDes",
    # AES-128
    Aes128 = "aes128",
    # AES-128-GCM
    Aes128Gcm = "aes128Gcm",
    # AES-256-GCM
    Aes256Gcm = "aes256Gcm",
    # AES-192
    Aes192 = "aes192",
    # AES-192-GCM
    Aes192Gcm = "aes192Gcm",
    # ChaCha20Poly1305
    ChaCha20Poly1305 = "chaCha20Poly1305",

