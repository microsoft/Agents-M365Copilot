from enum import Enum

class PfsGroup(str, Enum):
    None_ = "none",
    Pfs1 = "pfs1",
    Pfs2 = "pfs2",
    Pfs14 = "pfs14",
    Pfs24 = "pfs24",
    Pfs2048 = "pfs2048",
    Pfsmm = "pfsmm",
    Ecp256 = "ecp256",
    Ecp384 = "ecp384",
    UnknownFutureValue = "unknownFutureValue",

