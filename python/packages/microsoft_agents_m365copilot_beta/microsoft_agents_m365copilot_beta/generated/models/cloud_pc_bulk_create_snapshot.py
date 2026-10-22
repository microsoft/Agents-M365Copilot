from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_blob_access_tier import CloudPcBlobAccessTier
    from .cloud_pc_bulk_action import CloudPcBulkAction

from .cloud_pc_bulk_action import CloudPcBulkAction

@dataclass
class CloudPcBulkCreateSnapshot(CloudPcBulkAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcBulkCreateSnapshot"
    # Indicates the access tier of the blob file that the snapshot is copied to. Possible values are hot, cool, cold, archive, and unknownFutureValue. The default value is hot. Read-Only.
    access_tier: Optional[CloudPcBlobAccessTier] = None
    # Indicates the unique identifier for Secure Azure Storage Account, which receives the restore points (snapshots). The value can't be modified after it's created. For example, '/subscriptions/06199b73-30a1-4922-8734-93feca64cdf6/resourceGroups/res2627/providers/Microsoft.Storage/storageAccounts/sto1125'. Read-Only.
    storage_account_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcBulkCreateSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkCreateSnapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkCreateSnapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_blob_access_tier import CloudPcBlobAccessTier
        from .cloud_pc_bulk_action import CloudPcBulkAction

        from .cloud_pc_blob_access_tier import CloudPcBlobAccessTier
        from .cloud_pc_bulk_action import CloudPcBulkAction

        fields: dict[str, Callable[[Any], None]] = {
            "accessTier": lambda n : setattr(self, 'access_tier', n.get_enum_value(CloudPcBlobAccessTier)),
            "storageAccountId": lambda n : setattr(self, 'storage_account_id', n.get_str_value()),
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
        writer.write_enum_value("accessTier", self.access_tier)
        writer.write_str_value("storageAccountId", self.storage_account_id)
    

