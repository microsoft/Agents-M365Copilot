from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_metadata import AgentMetadata
    from .policy_location_application import PolicyLocationApplication

from .policy_location_application import PolicyLocationApplication

@dataclass
class PolicyLocationAgent(PolicyLocationApplication, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.policyLocationAgent"
    # The agentMetadata property
    agent_metadata: Optional[AgentMetadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyLocationAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyLocationAgent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyLocationAgent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_metadata import AgentMetadata
        from .policy_location_application import PolicyLocationApplication

        from .agent_metadata import AgentMetadata
        from .policy_location_application import PolicyLocationApplication

        fields: dict[str, Callable[[Any], None]] = {
            "agentMetadata": lambda n : setattr(self, 'agent_metadata', n.get_object_value(AgentMetadata)),
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
        writer.write_object_value("agentMetadata", self.agent_metadata)
    

