from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AssignedComputeInstanceDetails(Entity, Parsable):
    # Represents a set of S3 buckets accessed by this EC2 instance.
    accessed_storage_buckets: Optional[list[AuthorizationSystemResource]] = None
    # assigned EC2 instance.
    assigned_compute_instance: Optional[AuthorizationSystemResource] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignedComputeInstanceDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignedComputeInstanceDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignedComputeInstanceDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .entity import Entity

        from .authorization_system_resource import AuthorizationSystemResource
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessedStorageBuckets": lambda n : setattr(self, 'accessed_storage_buckets', n.get_collection_of_object_values(AuthorizationSystemResource)),
            "assignedComputeInstance": lambda n : setattr(self, 'assigned_compute_instance', n.get_object_value(AuthorizationSystemResource)),
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
        writer.write_collection_of_object_values("accessedStorageBuckets", self.accessed_storage_buckets)
        writer.write_object_value("assignedComputeInstance", self.assigned_compute_instance)
    

