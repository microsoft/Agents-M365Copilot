from enum import Enum

class VpnLocalIdentifier(str, Enum):
    # Device Fully Qualified Domain Name
    DeviceFQDN = "deviceFQDN",
    # Empty
    Empty = "empty",
    # Client Certificate Subject Name
    ClientCertificateSubjectName = "clientCertificateSubjectName",

