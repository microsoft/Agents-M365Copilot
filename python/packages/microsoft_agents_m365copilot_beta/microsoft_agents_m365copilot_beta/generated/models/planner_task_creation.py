from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_creation_source_kind import PlannerCreationSourceKind
    from .planner_external_task_source import PlannerExternalTaskSource
    from .planner_teams_publication_info import PlannerTeamsPublicationInfo

@dataclass
class PlannerTaskCreation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies what kind of creation source the task is created with. The possible values are: external, publication and unknownFutureValue.
    creation_source_kind: Optional[PlannerCreationSourceKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the publication process that created this task. This field is deprecated and clients should move to using the new inheritance model.
    teams_publication_info: Optional[PlannerTeamsPublicationInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskCreation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskCreation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerExternalTaskSource".casefold():
            from .planner_external_task_source import PlannerExternalTaskSource

            return PlannerExternalTaskSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTeamsPublicationInfo".casefold():
            from .planner_teams_publication_info import PlannerTeamsPublicationInfo

            return PlannerTeamsPublicationInfo()
        return PlannerTaskCreation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_creation_source_kind import PlannerCreationSourceKind
        from .planner_external_task_source import PlannerExternalTaskSource
        from .planner_teams_publication_info import PlannerTeamsPublicationInfo

        from .planner_creation_source_kind import PlannerCreationSourceKind
        from .planner_external_task_source import PlannerExternalTaskSource
        from .planner_teams_publication_info import PlannerTeamsPublicationInfo

        fields: dict[str, Callable[[Any], None]] = {
            "creationSourceKind": lambda n : setattr(self, 'creation_source_kind', n.get_enum_value(PlannerCreationSourceKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "teamsPublicationInfo": lambda n : setattr(self, 'teams_publication_info', n.get_object_value(PlannerTeamsPublicationInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("creationSourceKind", self.creation_source_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("teamsPublicationInfo", self.teams_publication_info)
        writer.write_additional_data_value(self.additional_data)
    

