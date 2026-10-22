from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_management_entity import CaseManagementEntity
    from .incident_relation import IncidentRelation
    from .recommendation_relation import RecommendationRelation
    from .workspace_indicator_relation import WorkspaceIndicatorRelation

from .case_management_entity import CaseManagementEntity

@dataclass
class Relation(CaseManagementEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.relation"
    # The identifier of the related external resource.
    related_resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Relation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Relation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.incidentRelation".casefold():
            from .incident_relation import IncidentRelation

            return IncidentRelation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.recommendationRelation".casefold():
            from .recommendation_relation import RecommendationRelation

            return RecommendationRelation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.workspaceIndicatorRelation".casefold():
            from .workspace_indicator_relation import WorkspaceIndicatorRelation

            return WorkspaceIndicatorRelation()
        return Relation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_management_entity import CaseManagementEntity
        from .incident_relation import IncidentRelation
        from .recommendation_relation import RecommendationRelation
        from .workspace_indicator_relation import WorkspaceIndicatorRelation

        from .case_management_entity import CaseManagementEntity
        from .incident_relation import IncidentRelation
        from .recommendation_relation import RecommendationRelation
        from .workspace_indicator_relation import WorkspaceIndicatorRelation

        fields: dict[str, Callable[[Any], None]] = {
            "relatedResourceId": lambda n : setattr(self, 'related_resource_id', n.get_str_value()),
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
        writer.write_str_value("relatedResourceId", self.related_resource_id)
    

