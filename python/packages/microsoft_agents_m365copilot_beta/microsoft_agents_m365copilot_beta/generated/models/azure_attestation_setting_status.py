from enum import Enum

class AzureAttestationSettingStatus(str, Enum):
    # Indicates that the device is not a Windows 11 device.
    NotApplicable = "notApplicable",
    # Indicates that the device has the Azure attestation setting enabled.
    Enabled = "enabled",
    # Indicates that the device has the Azure attestation setting disabled.
    Disabled = "disabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

