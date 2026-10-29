from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..directory_object import DirectoryObject
    from ..entity import Entity
    from .allotment import Allotment

from ..entity import Entity

@dataclass
class Assignment(Entity, Parsable):
    # The allotment from which licenses are assigned. Not nullable.
    allotment: Optional[Allotment] = None
    # The assignedTo property
    assigned_to: Optional[DirectoryObject] = None
    # The list of disabled service plans for this assignment. Not nullable.
    disabled_service_plan_ids: Optional[list[UUID]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Assignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Assignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Assignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from .allotment import Allotment

        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from .allotment import Allotment

        fields: dict[str, Callable[[Any], None]] = {
            "allotment": lambda n : setattr(self, 'allotment', n.get_object_value(Allotment)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(DirectoryObject)),
            "disabledServicePlanIds": lambda n : setattr(self, 'disabled_service_plan_ids', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_object_value("allotment", self.allotment)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_collection_of_primitive_values("disabledServicePlanIds", self.disabled_service_plan_ids)
    

