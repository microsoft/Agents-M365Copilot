from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_usage import ConfigurationUsage
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsIdentityProtectionConfiguration(DeviceConfiguration, Parsable):
    """
    This entity provides descriptions of the declared methods, properties and relationships exposed by Windows Hello for Business.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsIdentityProtectionConfiguration"
    # Boolean value used to enable enhanced anti-spoofing for facial feature recognition on Windows Hello face authentication.
    enhanced_anti_spoofing_for_facial_features_enabled: Optional[bool] = None
    # Integer value specifies the period (in days) that a PIN can be used before the system requires the user to change it. Valid values are 0 to 730 inclusive. Valid values 0 to 730
    pin_expiration_in_days: Optional[int] = None
    # Possible values of the ConfigurationUsage list.
    pin_lowercase_characters_usage: Optional[ConfigurationUsage] = None
    # Integer value that sets the maximum number of characters allowed for the work PIN. Valid values are 4 to 127 inclusive and greater than or equal to the value set for the minimum PIN. Valid values 4 to 127
    pin_maximum_length: Optional[int] = None
    # Integer value that sets the minimum number of characters required for the Windows Hello for Business PIN. Valid values are 4 to 127 inclusive and less than or equal to the value set for the maximum PIN. Valid values 4 to 127
    pin_minimum_length: Optional[int] = None
    # Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset. Valid values 0 to 50
    pin_previous_block_count: Optional[int] = None
    # Boolean value that enables a user to change their PIN by using the Windows Hello for Business PIN recovery service.
    pin_recovery_enabled: Optional[bool] = None
    # Possible values of the ConfigurationUsage list.
    pin_special_characters_usage: Optional[ConfigurationUsage] = None
    # Possible values of the ConfigurationUsage list.
    pin_uppercase_characters_usage: Optional[ConfigurationUsage] = None
    # Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
    security_device_required: Optional[bool] = None
    # Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
    unlock_with_biometrics_enabled: Optional[bool] = None
    # Boolean value that enables Windows Hello for Business to use certificates to authenticate on-premise resources.
    use_certificates_for_on_premises_auth_enabled: Optional[bool] = None
    # Boolean value used to enable the Windows Hello security key as a logon credential.
    use_security_key_for_signin: Optional[bool] = None
    # Boolean value that blocks Windows Hello for Business as a method for signing into Windows.
    windows_hello_for_business_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsIdentityProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsIdentityProtectionConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsIdentityProtectionConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .configuration_usage import ConfigurationUsage
        from .device_configuration import DeviceConfiguration

        from .configuration_usage import ConfigurationUsage
        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "enhancedAntiSpoofingForFacialFeaturesEnabled": lambda n : setattr(self, 'enhanced_anti_spoofing_for_facial_features_enabled', n.get_bool_value()),
            "pinExpirationInDays": lambda n : setattr(self, 'pin_expiration_in_days', n.get_int_value()),
            "pinLowercaseCharactersUsage": lambda n : setattr(self, 'pin_lowercase_characters_usage', n.get_enum_value(ConfigurationUsage)),
            "pinMaximumLength": lambda n : setattr(self, 'pin_maximum_length', n.get_int_value()),
            "pinMinimumLength": lambda n : setattr(self, 'pin_minimum_length', n.get_int_value()),
            "pinPreviousBlockCount": lambda n : setattr(self, 'pin_previous_block_count', n.get_int_value()),
            "pinRecoveryEnabled": lambda n : setattr(self, 'pin_recovery_enabled', n.get_bool_value()),
            "pinSpecialCharactersUsage": lambda n : setattr(self, 'pin_special_characters_usage', n.get_enum_value(ConfigurationUsage)),
            "pinUppercaseCharactersUsage": lambda n : setattr(self, 'pin_uppercase_characters_usage', n.get_enum_value(ConfigurationUsage)),
            "securityDeviceRequired": lambda n : setattr(self, 'security_device_required', n.get_bool_value()),
            "unlockWithBiometricsEnabled": lambda n : setattr(self, 'unlock_with_biometrics_enabled', n.get_bool_value()),
            "useCertificatesForOnPremisesAuthEnabled": lambda n : setattr(self, 'use_certificates_for_on_premises_auth_enabled', n.get_bool_value()),
            "useSecurityKeyForSignin": lambda n : setattr(self, 'use_security_key_for_signin', n.get_bool_value()),
            "windowsHelloForBusinessBlocked": lambda n : setattr(self, 'windows_hello_for_business_blocked', n.get_bool_value()),
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
        writer.write_bool_value("enhancedAntiSpoofingForFacialFeaturesEnabled", self.enhanced_anti_spoofing_for_facial_features_enabled)
        writer.write_int_value("pinExpirationInDays", self.pin_expiration_in_days)
        writer.write_enum_value("pinLowercaseCharactersUsage", self.pin_lowercase_characters_usage)
        writer.write_int_value("pinMaximumLength", self.pin_maximum_length)
        writer.write_int_value("pinMinimumLength", self.pin_minimum_length)
        writer.write_int_value("pinPreviousBlockCount", self.pin_previous_block_count)
        writer.write_bool_value("pinRecoveryEnabled", self.pin_recovery_enabled)
        writer.write_enum_value("pinSpecialCharactersUsage", self.pin_special_characters_usage)
        writer.write_enum_value("pinUppercaseCharactersUsage", self.pin_uppercase_characters_usage)
        writer.write_bool_value("securityDeviceRequired", self.security_device_required)
        writer.write_bool_value("unlockWithBiometricsEnabled", self.unlock_with_biometrics_enabled)
        writer.write_bool_value("useCertificatesForOnPremisesAuthEnabled", self.use_certificates_for_on_premises_auth_enabled)
        writer.write_bool_value("useSecurityKeyForSignin", self.use_security_key_for_signin)
        writer.write_bool_value("windowsHelloForBusinessBlocked", self.windows_hello_for_business_blocked)
    

