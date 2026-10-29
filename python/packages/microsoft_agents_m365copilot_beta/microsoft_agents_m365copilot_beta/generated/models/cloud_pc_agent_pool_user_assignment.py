from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_pool_assignment import CloudPcPoolAssignment

from .cloud_pc_pool_assignment import CloudPcPoolAssignment

@dataclass
class CloudPcAgentPoolUserAssignment(CloudPcPoolAssignment, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcAgentPoolUserAssignment"
    # The unique identifier of the user principal.
    user_principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAgentPoolUserAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAgentPoolUserAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAgentPoolUserAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_pool_assignment import CloudPcPoolAssignment

        from .cloud_pc_pool_assignment import CloudPcPoolAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "userPrincipalId": lambda n : setattr(self, 'user_principal_id', n.get_str_value()),
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
        writer.write_str_value("userPrincipalId", self.user_principal_id)
    

