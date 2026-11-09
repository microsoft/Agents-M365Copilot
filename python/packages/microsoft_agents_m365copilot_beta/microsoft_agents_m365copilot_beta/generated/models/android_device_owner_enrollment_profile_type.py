from enum import Enum

class AndroidDeviceOwnerEnrollmentProfileType(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Dedicated device.
    DedicatedDevice = "dedicatedDevice",
    # Fully managed.
    FullyManaged = "fullyManaged",

