from enum import Enum

class DeviceManagementCertificationAuthority(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Microsoft Certification Authority type.
    Microsoft = "microsoft",
    # DigiCert Certification Authority type.
    DigiCert = "digiCert",

