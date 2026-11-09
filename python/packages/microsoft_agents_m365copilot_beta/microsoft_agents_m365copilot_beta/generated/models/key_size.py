from enum import Enum

class KeySize(str, Enum):
    # 1024 Bits.
    Size1024 = "size1024",
    # 2048 Bits.
    Size2048 = "size2048",
    # 4096 Bits.
    Size4096 = "size4096",

