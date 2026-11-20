from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .resource_policy_assignment import ResourcePolicyAssignment
    from .resource_policy_definition import ResourcePolicyDefinition

from .entity import Entity

@dataclass
class ResourcePolicyDeletableRoot(Entity, Parsable):
    # The assignments property
    assignments: Optional[list[ResourcePolicyAssignment]] = None
    # The definitions property
    definitions: Optional[list[ResourcePolicyDefinition]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourcePolicyDeletableRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourcePolicyDeletableRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourcePolicyDeletableRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .resource_policy_assignment import ResourcePolicyAssignment
        from .resource_policy_definition import ResourcePolicyDefinition

        from .entity import Entity
        from .resource_policy_assignment import ResourcePolicyAssignment
        from .resource_policy_definition import ResourcePolicyDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(ResourcePolicyAssignment)),
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(ResourcePolicyDefinition)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("definitions", self.definitions)
    

