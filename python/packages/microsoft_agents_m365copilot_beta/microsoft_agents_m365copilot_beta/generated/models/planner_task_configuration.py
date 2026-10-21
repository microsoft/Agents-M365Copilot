from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_task_policy import PlannerTaskPolicy

from .entity import Entity

@dataclass
class PlannerTaskConfiguration(Entity, Parsable):
    # Policy configuration for tasks created for the businessScenario when they're being changed outside of the scenario.
    edit_policy: Optional[PlannerTaskPolicy] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_task_policy import PlannerTaskPolicy

        from .entity import Entity
        from .planner_task_policy import PlannerTaskPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "editPolicy": lambda n : setattr(self, 'edit_policy', n.get_object_value(PlannerTaskPolicy)),
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
        writer.write_object_value("editPolicy", self.edit_policy)
    

