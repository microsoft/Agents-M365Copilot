from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_external_task_source_display_type import PlannerExternalTaskSourceDisplayType
    from .planner_task_creation import PlannerTaskCreation

from .planner_task_creation import PlannerTaskCreation

@dataclass
class PlannerExternalTaskSource(PlannerTaskCreation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.plannerExternalTaskSource"
    # Nullable. An identifier for the scenario associated with this external source. This should be in reverse DNS format. For example, Contoso company owned application for customer support would have a value like 'com.constoso.customerSupport'.
    context_scenario_id: Optional[str] = None
    # Specifies how an application should display the link to the associated plannerExternalTaskSource. The possible values are: none, default.
    display_link_type: Optional[PlannerExternalTaskSourceDisplayType] = None
    # The segments of the name of the external experience. Segments represent a hierarchical structure that allows other apps to display the relationship.
    display_name_segments: Optional[list[str]] = None
    # Nullable. The id of the external entity's containing entity or context.
    external_context_id: Optional[str] = None
    # Nullable. The id of the entity that an external service associates with a task.
    external_object_id: Optional[str] = None
    # Nullable. The external Item Version for the object specified by the externalObjectId.
    external_object_version: Optional[str] = None
    # Nullable. URL of the user experience represented by the associated plannerExternalTaskSource.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerExternalTaskSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerExternalTaskSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerExternalTaskSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_external_task_source_display_type import PlannerExternalTaskSourceDisplayType
        from .planner_task_creation import PlannerTaskCreation

        from .planner_external_task_source_display_type import PlannerExternalTaskSourceDisplayType
        from .planner_task_creation import PlannerTaskCreation

        fields: dict[str, Callable[[Any], None]] = {
            "contextScenarioId": lambda n : setattr(self, 'context_scenario_id', n.get_str_value()),
            "displayLinkType": lambda n : setattr(self, 'display_link_type', n.get_enum_value(PlannerExternalTaskSourceDisplayType)),
            "displayNameSegments": lambda n : setattr(self, 'display_name_segments', n.get_collection_of_primitive_values(str)),
            "externalContextId": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "externalObjectId": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
            "externalObjectVersion": lambda n : setattr(self, 'external_object_version', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_enum_value("displayLinkType", self.display_link_type)
        writer.write_collection_of_primitive_values("displayNameSegments", self.display_name_segments)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
        writer.write_str_value("externalObjectVersion", self.external_object_version)
        writer.write_str_value("webUrl", self.web_url)
    

