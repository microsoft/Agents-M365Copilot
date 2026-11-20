from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_plan_creation import PlannerPlanCreation

from .planner_plan_creation import PlannerPlanCreation

@dataclass
class PlannerExternalPlanSource(PlannerPlanCreation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.plannerExternalPlanSource"
    # Nullable. An identifier for the scenario associated with this external source. This should be in reverse DNS format. For example, Contoso company owned application for customer support would have a value like 'com.constoso.customerSupport'.
    context_scenario_id: Optional[str] = None
    # Nullable. The ID of the external entity's containing entity or context.
    external_context_id: Optional[str] = None
    # Nullable. The ID of the entity that an external service associates with a plan.
    external_object_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerExternalPlanSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerExternalPlanSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerExternalPlanSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_plan_creation import PlannerPlanCreation

        from .planner_plan_creation import PlannerPlanCreation

        fields: dict[str, Callable[[Any], None]] = {
            "contextScenarioId": lambda n : setattr(self, 'context_scenario_id', n.get_str_value()),
            "externalContextId": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "externalObjectId": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
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
        writer.write_str_value("contextScenarioId", self.context_scenario_id)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
    

