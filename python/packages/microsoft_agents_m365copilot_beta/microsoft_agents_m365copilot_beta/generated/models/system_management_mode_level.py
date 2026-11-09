from enum import Enum

class SystemManagementModeLevel(str, Enum):
    # Indicates that the device does not have Firmware protection (System Management Mode) enabled.
    NotApplicable = "notApplicable",
    # Indicates that deny System Management Mode (SMM) read/write access to OS and Virtualization-based security (VBS) memory. The benefit is that by design System Management Mode (SMM) cannot modify security of or exfiltrate secrets from the OS (including Virtualization-based security).
    Level1 = "level1",
    # Indicates that in addition to the System Management Mode (SMM) Level 1 protections, this level prevents System Management Mode (SMM) from tampering with Input-Output Memory Management Unit (IOMMU) config. The benefit is that by design System Management Mode (SMM) cannot disable Virtualization-based security (VBS) and kernel Direct memory access (DMA) protections.
    Level2 = "level2",
    # Indicates that in addition to the System Management Mode (SMM) Level 2 protections, this level reduces System Management Mode (SMM) save state capabilities. The benefit is that by design System Management Mode (SMM) cannot exploit save state to modify security of or exfiltrate secrets from the OS (including Virtualization-based security).
    Level3 = "level3",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

