from enum import Enum

class CertificateDestinationStore(str, Enum):
    # Computer Certificate Store - Root.
    ComputerCertStoreRoot = "computerCertStoreRoot",
    # Computer Certificate Store - Intermediate.
    ComputerCertStoreIntermediate = "computerCertStoreIntermediate",
    # User Certificate Store - Intermediate.
    UserCertStoreIntermediate = "userCertStoreIntermediate",

