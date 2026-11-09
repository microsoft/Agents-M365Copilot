from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_bulk_action import CloudPcBulkAction
    from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration

from .cloud_pc_bulk_action import CloudPcBulkAction

@dataclass
class CloudPcBulkRelocate(CloudPcBulkAction, Parsable):
    """
    Represents the details of a bulk Cloud PC relocate action.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcBulkRelocate"
    # The domain join configurations used when relocating Cloud PCs.
    domain_join_configurations: Optional[list[CloudPcDomainJoinConfiguration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcBulkRelocate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkRelocate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkRelocate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration

        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "domainJoinConfigurations": lambda n : setattr(self, 'domain_join_configurations', n.get_collection_of_object_values(CloudPcDomainJoinConfiguration)),
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
        writer.write_collection_of_object_values("domainJoinConfigurations", self.domain_join_configurations)
    

