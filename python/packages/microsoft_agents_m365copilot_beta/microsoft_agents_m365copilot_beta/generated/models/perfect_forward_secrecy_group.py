from enum import Enum

class PerfectForwardSecrecyGroup(str, Enum):
    # PFS1
    Pfs1 = "pfs1",
    # PFS2
    Pfs2 = "pfs2",
    # PFS2048
    Pfs2048 = "pfs2048",
    # ECP256
    Ecp256 = "ecp256",
    # ECP384
    Ecp384 = "ecp384",
    # PFSMM
    PfsMM = "pfsMM",
    # PFS24
    Pfs24 = "pfs24",

