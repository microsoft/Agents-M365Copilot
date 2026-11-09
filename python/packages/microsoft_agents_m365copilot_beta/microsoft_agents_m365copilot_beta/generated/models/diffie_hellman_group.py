from enum import Enum

class DiffieHellmanGroup(str, Enum):
    # Group1
    Group1 = "group1",
    # Group2
    Group2 = "group2",
    # Group14
    Group14 = "group14",
    # ECP256
    Ecp256 = "ecp256",
    # ECP384
    Ecp384 = "ecp384",
    # Group24
    Group24 = "group24",

