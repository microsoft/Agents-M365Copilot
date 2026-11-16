from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bit_locker_recovery_information_type import BitLockerRecoveryInformationType
    from .configuration_usage import ConfigurationUsage

@dataclass
class BitLockerRecoveryOptions(AdditionalDataHolder, Parsable):
    """
    BitLocker Recovery Options.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether to block certificate-based data recovery agent.
    block_data_recovery_agent: Optional[bool] = None
    # Indicates whether or not to enable BitLocker until recovery information is stored in AD DS.
    enable_bit_locker_after_recovery_information_to_store: Optional[bool] = None
    # Indicates whether or not to allow BitLocker recovery information to store in AD DS.
    enable_recovery_information_save_to_store: Optional[bool] = None
    # Indicates whether or not to allow showing recovery options in BitLocker Setup Wizard for fixed or system disk.
    hide_recovery_options: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # BitLockerRecoveryInformationType types
    recovery_information_to_store: Optional[BitLockerRecoveryInformationType] = None
    # Possible values of the ConfigurationUsage list.
    recovery_key_usage: Optional[ConfigurationUsage] = None
    # Possible values of the ConfigurationUsage list.
    recovery_password_usage: Optional[ConfigurationUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BitLockerRecoveryOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerRecoveryOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BitLockerRecoveryOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bit_locker_recovery_information_type import BitLockerRecoveryInformationType
        from .configuration_usage import ConfigurationUsage

        from .bit_locker_recovery_information_type import BitLockerRecoveryInformationType
        from .configuration_usage import ConfigurationUsage

        fields: dict[str, Callable[[Any], None]] = {
            "blockDataRecoveryAgent": lambda n : setattr(self, 'block_data_recovery_agent', n.get_bool_value()),
            "enableBitLockerAfterRecoveryInformationToStore": lambda n : setattr(self, 'enable_bit_locker_after_recovery_information_to_store', n.get_bool_value()),
            "enableRecoveryInformationSaveToStore": lambda n : setattr(self, 'enable_recovery_information_save_to_store', n.get_bool_value()),
            "hideRecoveryOptions": lambda n : setattr(self, 'hide_recovery_options', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recoveryInformationToStore": lambda n : setattr(self, 'recovery_information_to_store', n.get_enum_value(BitLockerRecoveryInformationType)),
            "recoveryKeyUsage": lambda n : setattr(self, 'recovery_key_usage', n.get_enum_value(ConfigurationUsage)),
            "recoveryPasswordUsage": lambda n : setattr(self, 'recovery_password_usage', n.get_enum_value(ConfigurationUsage)),
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
        writer.write_bool_value("blockDataRecoveryAgent", self.block_data_recovery_agent)
        writer.write_bool_value("enableBitLockerAfterRecoveryInformationToStore", self.enable_bit_locker_after_recovery_information_to_store)
        writer.write_bool_value("enableRecoveryInformationSaveToStore", self.enable_recovery_information_save_to_store)
        writer.write_bool_value("hideRecoveryOptions", self.hide_recovery_options)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recoveryInformationToStore", self.recovery_information_to_store)
        writer.write_enum_value("recoveryKeyUsage", self.recovery_key_usage)
        writer.write_enum_value("recoveryPasswordUsage", self.recovery_password_usage)
        writer.write_additional_data_value(self.additional_data)
    

