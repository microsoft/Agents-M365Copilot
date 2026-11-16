from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
    from .device_compliance_policy import DeviceCompliancePolicy

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class AospDeviceOwnerCompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the AndroidDeviceOwnerAOSPCompliancePolicy resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.aospDeviceOwnerCompliancePolicy"
    # Minimum Android security patch level.
    min_android_security_patch_level: Optional[str] = None
    # Maximum Android version.
    os_maximum_version: Optional[str] = None
    # Minimum Android version.
    os_minimum_version: Optional[str] = None
    # Minimum password length. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before a password is required. Valid values 1 to 8640
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Require a password to unlock device.
    password_required: Optional[bool] = None
    # Type of characters in password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
    password_required_type: Optional[AndroidDeviceOwnerRequiredPasswordType] = None
    # Indicates the device should not be rooted. When TRUE, if the device is detected as rooted it will be reported non-compliant. When FALSE, the device is not reported as non-compliant regardless of device rooted state. Default is FALSE.
    security_block_jailbroken_devices: Optional[bool] = None
    # Require encryption on Android devices.
    storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AospDeviceOwnerCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AospDeviceOwnerCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AospDeviceOwnerCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .device_compliance_policy import DeviceCompliancePolicy

        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .device_compliance_policy import DeviceCompliancePolicy

        fields: dict[str, Callable[[Any], None]] = {
            "minAndroidSecurityPatchLevel": lambda n : setattr(self, 'min_android_security_patch_level', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordType)),
            "securityBlockJailbrokenDevices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
            "storageRequireEncryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("minAndroidSecurityPatchLevel", self.min_android_security_patch_level)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("securityBlockJailbrokenDevices", self.security_block_jailbroken_devices)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    

