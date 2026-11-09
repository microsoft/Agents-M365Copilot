from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bit_locker_encryption_method import BitLockerEncryptionMethod
    from .bit_locker_recovery_options import BitLockerRecoveryOptions

@dataclass
class BitLockerFixedDrivePolicy(AdditionalDataHolder, Parsable):
    """
    BitLocker Fixed Drive Policies.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Select the encryption method for fixed drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
    encryption_method: Optional[BitLockerEncryptionMethod] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This policy setting allows you to control how BitLocker-protected fixed data drives are recovered in the absence of the required credentials. This policy setting is applied when you turn on BitLocker.
    recovery_options: Optional[BitLockerRecoveryOptions] = None
    # This policy setting determines whether BitLocker protection is required for fixed data drives to be writable on a computer.
    require_encryption_for_write_access: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BitLockerFixedDrivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerFixedDrivePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BitLockerFixedDrivePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bit_locker_encryption_method import BitLockerEncryptionMethod
        from .bit_locker_recovery_options import BitLockerRecoveryOptions

        from .bit_locker_encryption_method import BitLockerEncryptionMethod
        from .bit_locker_recovery_options import BitLockerRecoveryOptions

        fields: dict[str, Callable[[Any], None]] = {
            "encryptionMethod": lambda n : setattr(self, 'encryption_method', n.get_enum_value(BitLockerEncryptionMethod)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recoveryOptions": lambda n : setattr(self, 'recovery_options', n.get_object_value(BitLockerRecoveryOptions)),
            "requireEncryptionForWriteAccess": lambda n : setattr(self, 'require_encryption_for_write_access', n.get_bool_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recoveryOptions", self.recovery_options)
        writer.write_bool_value("requireEncryptionForWriteAccess", self.require_encryption_for_write_access)
        writer.write_additional_data_value(self.additional_data)
    

