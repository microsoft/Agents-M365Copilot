from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .azure_encryption import AzureEncryption
    from .finding import Finding

from .finding import Finding

@dataclass
class EncryptedAzureStorageAccountFinding(Finding, Parsable):
    # The encryptionManagedBy property
    encryption_managed_by: Optional[AzureEncryption] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The storageAccount property
    storage_account: Optional[AuthorizationSystemResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EncryptedAzureStorageAccountFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptedAzureStorageAccountFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EncryptedAzureStorageAccountFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .azure_encryption import AzureEncryption
        from .finding import Finding

        from .authorization_system_resource import AuthorizationSystemResource
        from .azure_encryption import AzureEncryption
        from .finding import Finding

        fields: dict[str, Callable[[Any], None]] = {
            "encryptionManagedBy": lambda n : setattr(self, 'encryption_managed_by', n.get_enum_value(AzureEncryption)),
            "storageAccount": lambda n : setattr(self, 'storage_account', n.get_object_value(AuthorizationSystemResource)),
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
        writer.write_enum_value("encryptionManagedBy", self.encryption_managed_by)
        writer.write_object_value("storageAccount", self.storage_account)
    

