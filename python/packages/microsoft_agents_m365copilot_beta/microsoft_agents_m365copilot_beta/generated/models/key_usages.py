from enum import Enum

class KeyUsages(str, Enum):
    # Key Encipherment Usage.
    KeyEncipherment = "keyEncipherment",
    # Digital Signature Usage.
    DigitalSignature = "digitalSignature",

