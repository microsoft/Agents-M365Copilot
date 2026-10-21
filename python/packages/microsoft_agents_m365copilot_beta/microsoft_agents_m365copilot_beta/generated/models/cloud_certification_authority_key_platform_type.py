from enum import Enum

class CloudCertificationAuthorityKeyPlatformType(str, Enum):
    # Default. The key platform type is unknown or invalid.
    Unknown = "unknown",
    # The certification authority keys are stored in software.
    Software = "software",
    # The certification authority keys are stored in a hardware security module.
    HardwareSecurityModule = "hardwareSecurityModule",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

