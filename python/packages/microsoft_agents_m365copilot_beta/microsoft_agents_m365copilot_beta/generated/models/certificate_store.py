from enum import Enum

class CertificateStore(str, Enum):
    User = "user",
    Machine = "machine",

