from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..subject_set import SubjectSet
    from .agent_builder_platforms import AgentBuilderPlatforms

from ..subject_set import SubjectSet

@dataclass
class SelectedAgentBuilderPlatformsSubjectSet(SubjectSet, Parsable):
    """
    Defines the scope as only agent identities created by any of the selected builder platforms. It is valid only for agent identity lifecycle policies; using it on another policy type returns HTTP 400.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.selectedAgentBuilderPlatformsSubjectSet"
    # The includedAgentBuilderPlatforms property
    included_agent_builder_platforms: Optional[AgentBuilderPlatforms] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelectedAgentBuilderPlatformsSubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelectedAgentBuilderPlatformsSubjectSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelectedAgentBuilderPlatformsSubjectSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..subject_set import SubjectSet
        from .agent_builder_platforms import AgentBuilderPlatforms

        from ..subject_set import SubjectSet
        from .agent_builder_platforms import AgentBuilderPlatforms

        fields: dict[str, Callable[[Any], None]] = {
            "includedAgentBuilderPlatforms": lambda n : setattr(self, 'included_agent_builder_platforms', n.get_collection_of_enum_values(AgentBuilderPlatforms)),
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
        writer.write_enum_value("includedAgentBuilderPlatforms", self.included_agent_builder_platforms)
    

