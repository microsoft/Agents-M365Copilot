from enum import Enum

class DiscoverySource(str, Enum):
    # DiscoverySource is Unknown.
    Unknown = "unknown",
    # Device is imported by admin.
    AdminImport = "adminImport",
    # Device is added by Apple device enrollment program (Dep).
    DeviceEnrollmentProgram = "deviceEnrollmentProgram",

