from enum import Enum

class EndpointSecurityConfigurationType(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # Antivirus.
    Antivirus = "antivirus",
    # Disk encryption.
    DiskEncryption = "diskEncryption",
    # Firewall.
    Firewall = "firewall",
    # Endpoint detection and response.
    EndpointDetectionAndResponse = "endpointDetectionAndResponse",
    # Attack surface reduction.
    AttackSurfaceReduction = "attackSurfaceReduction",
    # Account protection.
    AccountProtection = "accountProtection",

