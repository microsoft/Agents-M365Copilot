from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
    from .android_safety_net_evaluation_type import AndroidSafetyNetEvaluationType
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_threat_protection_level import DeviceThreatProtectionLevel

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class AndroidDeviceOwnerCompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the AndroidDeviceOwnerCompliancePolicy resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerCompliancePolicy"
    # Indicates the Microsoft Defender for Endpoint (also referred to Microsoft Defender Advanced Threat Protection (MDATP)) minimum risk level to report noncompliance. Possible values are: unavailable, secured, low, medium, high, notSet. Possible values are: unavailable, secured, low, medium, high, notSet.
    advanced_threat_protection_required_security_level: Optional[DeviceThreatProtectionLevel] = None
    # Indicates whether the policy requires devices have device threat protection enabled.  When TRUE, threat protection is enabled.  When FALSE, threat protection is not enabled.  Default is FALSE.
    device_threat_protection_enabled: Optional[bool] = None
    # Indicates the minimum mobile threat protection risk level to that results in Intune reporting device noncompliance. Possible values are: unavailable, secured, low, medium, high, notSet. Possible values are: unavailable, secured, low, medium, high, notSet.
    device_threat_protection_required_security_level: Optional[DeviceThreatProtectionLevel] = None
    # Indicates the minimum Android security patch level required to mark the device as compliant.  For example: 'February 1, 2025'
    min_android_security_patch_level: Optional[str] = None
    # Indicates the maximum Android version required to mark the device as compliant.  For example: '15'
    os_maximum_version: Optional[str] = None
    # Indicates the minimum Android version required to mark the device as compliant. For example: '14'
    os_minimum_version: Optional[str] = None
    # Indicates the number of days before the password expires. Valid values 1 to 365.
    password_expiration_days: Optional[int] = None
    # Indicates the minimum password length required to mark the device as compliant. Valid values are 4 to 16, inclusive. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Indicates the minimum number of letter characters required for device password for the device to be marked compliant. Valid values 1 to 16.
    password_minimum_letter_characters: Optional[int] = None
    # Indicates the minimum number of lower case characters required for device password for the device to be marked compliant. Valid values 1 to 16.
    password_minimum_lower_case_characters: Optional[int] = None
    # Indicates the minimum number of non-letter characters required for device password for the device to be marked compliant. Valid values 1 to 16.
    password_minimum_non_letter_characters: Optional[int] = None
    # Indicates the minimum number of numeric characters required for device password for the device to be marked compliant. Valid values 1 to 16.
    password_minimum_numeric_characters: Optional[int] = None
    # Indicates the minimum number of symbol characters required for device password for the device to be marked compliant. Valid values 1 to 16.
    password_minimum_symbol_characters: Optional[int] = None
    # Indicates the minimum number of upper case letter characters required for device password for the device to be marked compliant. Valid values 1 to 16.
    password_minimum_upper_case_characters: Optional[int] = None
    # Indicates the number of minutes of inactivity before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Indicates the number of previous passwords to block. Valid values 1 to 24.
    password_previous_password_count_to_block: Optional[int] = None
    # Indicates whether a password is required to unlock the device. When TRUE, there must be a password set that unlocks the device for the device to be marked as compliant.  When FALSE, a device is marked as compliant whether or not a password is set as required to unlock the device.  Default is FALSE.
    password_required: Optional[bool] = None
    # Indicates the password complexity requirement for the device to be marked compliant. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
    password_required_type: Optional[AndroidDeviceOwnerRequiredPasswordType] = None
    # Indicates whether the device has pending security or OS updates and sets the compliance state accordingly.  When TRUE, checks if there are any pending system updates on each check in and if there are any pending security or OS version updates (System Updates), the device will be reported as non-compliant. If set to FALSE, then checks for any pending security or OS version updates (System Updates) are done without impact to device compliance state. Default is FALSE.
    require_no_pending_system_updates: Optional[bool] = None
    # Indicates the device should not be rooted. When TRUE, if the device is detected as rooted it will be reported non-compliant. When FALSE, the device is not reported as non-compliant regardless of device rooted state. Default is FALSE.
    security_block_jailbroken_devices: Optional[bool] = None
    # Indicates whether Intune application integrity is required to mark the device as compliant.  When TRUE, Intune checks that the Intune app installed on fully managed, dedicated, or corporate-owned work profile Android Enterprise enrolled devices, is the one provided by Microsoft from the Managed Google Play store. If the check fails, the device will be reported as non-compliant. Default is FALSE.
    security_require_intune_app_integrity: Optional[bool] = None
    # Indicates whether the compliance check will validate the Google Play Integrity check. When TRUE, the Google Play integrity basic check must pass to consider the device compliant.  When FALSE, the Google Play integrity basic check can pass or fail and the device will be considered compliant.  Default is FALSE.
    security_require_safety_net_attestation_basic_integrity: Optional[bool] = None
    # Indicates whether the compliance check will validate the Google Play Integrity check. When TRUE, the Google Play integrity device check must pass to consider the device compliant.  When FALSE, the Google Play integrity device check can pass or fail and the device will be considered compliant.  Default is FALSE.
    security_require_safety_net_attestation_certified_device: Optional[bool] = None
    # Indicates the types of measurements and reference data used to evaluate the device SafetyNet evaluation. Evaluation is completed on the device to assess device integrity based on checks defined by Android and built into the device hardware, for example, compromised OS version or root detection. Possible values are: basic, hardwareBacked, with default value of basic. Possible values are: basic, hardwareBacked.
    security_required_android_safety_net_evaluation_type: Optional[AndroidSafetyNetEvaluationType] = None
    # Indicates whether encryption on Android devices is required to mark the device as compliant.
    storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .android_safety_net_evaluation_type import AndroidSafetyNetEvaluationType
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel

        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .android_safety_net_evaluation_type import AndroidSafetyNetEvaluationType
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel

        fields: dict[str, Callable[[Any], None]] = {
            "advancedThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'advanced_threat_protection_required_security_level', n.get_enum_value(DeviceThreatProtectionLevel)),
            "deviceThreatProtectionEnabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "deviceThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(DeviceThreatProtectionLevel)),
            "minAndroidSecurityPatchLevel": lambda n : setattr(self, 'min_android_security_patch_level', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinimumLetterCharacters": lambda n : setattr(self, 'password_minimum_letter_characters', n.get_int_value()),
            "passwordMinimumLowerCaseCharacters": lambda n : setattr(self, 'password_minimum_lower_case_characters', n.get_int_value()),
            "passwordMinimumNonLetterCharacters": lambda n : setattr(self, 'password_minimum_non_letter_characters', n.get_int_value()),
            "passwordMinimumNumericCharacters": lambda n : setattr(self, 'password_minimum_numeric_characters', n.get_int_value()),
            "passwordMinimumSymbolCharacters": lambda n : setattr(self, 'password_minimum_symbol_characters', n.get_int_value()),
            "passwordMinimumUpperCaseCharacters": lambda n : setattr(self, 'password_minimum_upper_case_characters', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordCountToBlock": lambda n : setattr(self, 'password_previous_password_count_to_block', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordType)),
            "requireNoPendingSystemUpdates": lambda n : setattr(self, 'require_no_pending_system_updates', n.get_bool_value()),
            "securityBlockJailbrokenDevices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
            "securityRequireIntuneAppIntegrity": lambda n : setattr(self, 'security_require_intune_app_integrity', n.get_bool_value()),
            "securityRequireSafetyNetAttestationBasicIntegrity": lambda n : setattr(self, 'security_require_safety_net_attestation_basic_integrity', n.get_bool_value()),
            "securityRequireSafetyNetAttestationCertifiedDevice": lambda n : setattr(self, 'security_require_safety_net_attestation_certified_device', n.get_bool_value()),
            "securityRequiredAndroidSafetyNetEvaluationType": lambda n : setattr(self, 'security_required_android_safety_net_evaluation_type', n.get_enum_value(AndroidSafetyNetEvaluationType)),
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
        writer.write_enum_value("advancedThreatProtectionRequiredSecurityLevel", self.advanced_threat_protection_required_security_level)
        writer.write_bool_value("deviceThreatProtectionEnabled", self.device_threat_protection_enabled)
        writer.write_enum_value("deviceThreatProtectionRequiredSecurityLevel", self.device_threat_protection_required_security_level)
        writer.write_str_value("minAndroidSecurityPatchLevel", self.min_android_security_patch_level)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinimumLetterCharacters", self.password_minimum_letter_characters)
        writer.write_int_value("passwordMinimumLowerCaseCharacters", self.password_minimum_lower_case_characters)
        writer.write_int_value("passwordMinimumNonLetterCharacters", self.password_minimum_non_letter_characters)
        writer.write_int_value("passwordMinimumNumericCharacters", self.password_minimum_numeric_characters)
        writer.write_int_value("passwordMinimumSymbolCharacters", self.password_minimum_symbol_characters)
        writer.write_int_value("passwordMinimumUpperCaseCharacters", self.password_minimum_upper_case_characters)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordCountToBlock", self.password_previous_password_count_to_block)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("requireNoPendingSystemUpdates", self.require_no_pending_system_updates)
        writer.write_bool_value("securityBlockJailbrokenDevices", self.security_block_jailbroken_devices)
        writer.write_bool_value("securityRequireIntuneAppIntegrity", self.security_require_intune_app_integrity)
        writer.write_bool_value("securityRequireSafetyNetAttestationBasicIntegrity", self.security_require_safety_net_attestation_basic_integrity)
        writer.write_bool_value("securityRequireSafetyNetAttestationCertifiedDevice", self.security_require_safety_net_attestation_certified_device)
        writer.write_enum_value("securityRequiredAndroidSafetyNetEvaluationType", self.security_required_android_safety_net_evaluation_type)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    

