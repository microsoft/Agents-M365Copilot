from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bit_locker_encryption_method import BitLockerEncryptionMethod
    from .bit_locker_recovery_options import BitLockerRecoveryOptions
    from .configuration_usage import ConfigurationUsage

@dataclass
class BitLockerSystemDrivePolicy(AdditionalDataHolder, Parsable):
    """
    BitLocker Encryption Base Policies.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Select the encryption method for operating system drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
    encryption_method: Optional[BitLockerEncryptionMethod] = None
    # Indicates the minimum length of startup pin. Valid values 4 to 20
    minimum_pin_length: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Enable pre-boot recovery message and Url. If requireStartupAuthentication is false, this value does not affect.
    preboot_recovery_enable_message_and_url: Optional[bool] = None
    # Defines a custom recovery message.
    preboot_recovery_message: Optional[str] = None
    # Defines a custom recovery URL.
    preboot_recovery_url: Optional[str] = None
    # Allows to recover BitLocker encrypted operating system drives in the absence of the required startup key information. This policy setting is applied when you turn on BitLocker.
    recovery_options: Optional[BitLockerRecoveryOptions] = None
    # Indicates whether to allow BitLocker without a compatible TPM (requires a password or a startup key on a USB flash drive).
    startup_authentication_block_without_tpm_chip: Optional[bool] = None
    # Require additional authentication at startup.
    startup_authentication_required: Optional[bool] = None
    # Possible values of the ConfigurationUsage list.
    startup_authentication_tpm_key_usage: Optional[ConfigurationUsage] = None
    # Possible values of the ConfigurationUsage list.
    startup_authentication_tpm_pin_and_key_usage: Optional[ConfigurationUsage] = None
    # Possible values of the ConfigurationUsage list.
    startup_authentication_tpm_pin_usage: Optional[ConfigurationUsage] = None
    # Possible values of the ConfigurationUsage list.
    startup_authentication_tpm_usage: Optional[ConfigurationUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BitLockerSystemDrivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerSystemDrivePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BitLockerSystemDrivePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bit_locker_encryption_method import BitLockerEncryptionMethod
        from .bit_locker_recovery_options import BitLockerRecoveryOptions
        from .configuration_usage import ConfigurationUsage

        from .bit_locker_encryption_method import BitLockerEncryptionMethod
        from .bit_locker_recovery_options import BitLockerRecoveryOptions
        from .configuration_usage import ConfigurationUsage

        fields: dict[str, Callable[[Any], None]] = {
            "encryptionMethod": lambda n : setattr(self, 'encryption_method', n.get_enum_value(BitLockerEncryptionMethod)),
            "minimumPinLength": lambda n : setattr(self, 'minimum_pin_length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prebootRecoveryEnableMessageAndUrl": lambda n : setattr(self, 'preboot_recovery_enable_message_and_url', n.get_bool_value()),
            "prebootRecoveryMessage": lambda n : setattr(self, 'preboot_recovery_message', n.get_str_value()),
            "prebootRecoveryUrl": lambda n : setattr(self, 'preboot_recovery_url', n.get_str_value()),
            "recoveryOptions": lambda n : setattr(self, 'recovery_options', n.get_object_value(BitLockerRecoveryOptions)),
            "startupAuthenticationBlockWithoutTpmChip": lambda n : setattr(self, 'startup_authentication_block_without_tpm_chip', n.get_bool_value()),
            "startupAuthenticationRequired": lambda n : setattr(self, 'startup_authentication_required', n.get_bool_value()),
            "startupAuthenticationTpmKeyUsage": lambda n : setattr(self, 'startup_authentication_tpm_key_usage', n.get_enum_value(ConfigurationUsage)),
            "startupAuthenticationTpmPinAndKeyUsage": lambda n : setattr(self, 'startup_authentication_tpm_pin_and_key_usage', n.get_enum_value(ConfigurationUsage)),
            "startupAuthenticationTpmPinUsage": lambda n : setattr(self, 'startup_authentication_tpm_pin_usage', n.get_enum_value(ConfigurationUsage)),
            "startupAuthenticationTpmUsage": lambda n : setattr(self, 'startup_authentication_tpm_usage', n.get_enum_value(ConfigurationUsage)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_int_value("minimumPinLength", self.minimum_pin_length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("prebootRecoveryEnableMessageAndUrl", self.preboot_recovery_enable_message_and_url)
        writer.write_str_value("prebootRecoveryMessage", self.preboot_recovery_message)
        writer.write_str_value("prebootRecoveryUrl", self.preboot_recovery_url)
        writer.write_object_value("recoveryOptions", self.recovery_options)
        writer.write_bool_value("startupAuthenticationBlockWithoutTpmChip", self.startup_authentication_block_without_tpm_chip)
        writer.write_bool_value("startupAuthenticationRequired", self.startup_authentication_required)
        writer.write_enum_value("startupAuthenticationTpmKeyUsage", self.startup_authentication_tpm_key_usage)
        writer.write_enum_value("startupAuthenticationTpmPinAndKeyUsage", self.startup_authentication_tpm_pin_and_key_usage)
        writer.write_enum_value("startupAuthenticationTpmPinUsage", self.startup_authentication_tpm_pin_usage)
        writer.write_enum_value("startupAuthenticationTpmUsage", self.startup_authentication_tpm_usage)
        writer.write_additional_data_value(self.additional_data)
    

