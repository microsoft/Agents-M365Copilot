from enum import Enum

class AndroidManagedAppSafetyNetDeviceAttestationType(str, Enum):
    # no requirement set
    None_ = "none",
    # require that Android device passes SafetyNet Basic Integrity validation
    BasicIntegrity = "basicIntegrity",
    # require that Android device passes SafetyNet Basic Integrity and Device Certification validations
    BasicIntegrityAndDeviceCertification = "basicIntegrityAndDeviceCertification",

