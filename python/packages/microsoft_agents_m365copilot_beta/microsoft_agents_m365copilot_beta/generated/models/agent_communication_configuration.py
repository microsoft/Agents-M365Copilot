from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_endpoint_configuration import AgentEndpointConfiguration
    from .agent_teamwork_configuration import AgentTeamworkConfiguration
    from .entity import Entity

from .entity import Entity

@dataclass
class AgentCommunicationConfiguration(Entity, Parsable):
    # The endpoint binding (bot ID or callback URI) that the agent uses to receive messages.
    endpoint_configuration: Optional[AgentEndpointConfiguration] = None
    # Indicates whether individual agent instances created from this blueprint can override the endpointConfiguration. When true, each instance can override it; when false, every instance inherits it. Not nullable.
    is_overridable_at_agent_id_level: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The per-conversation-context message notification settings (group chat, channel, one-on-one chat, and meeting chat) that agents use.
    teamwork_configuration: Optional[AgentTeamworkConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentCommunicationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentCommunicationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentCommunicationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_endpoint_configuration import AgentEndpointConfiguration
        from .agent_teamwork_configuration import AgentTeamworkConfiguration
        from .entity import Entity

        from .agent_endpoint_configuration import AgentEndpointConfiguration
        from .agent_teamwork_configuration import AgentTeamworkConfiguration
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "endpointConfiguration": lambda n : setattr(self, 'endpoint_configuration', n.get_object_value(AgentEndpointConfiguration)),
            "isOverridableAtAgentIdLevel": lambda n : setattr(self, 'is_overridable_at_agent_id_level', n.get_bool_value()),
            "teamworkConfiguration": lambda n : setattr(self, 'teamwork_configuration', n.get_object_value(AgentTeamworkConfiguration)),
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
        writer.write_object_value("endpointConfiguration", self.endpoint_configuration)
        writer.write_bool_value("isOverridableAtAgentIdLevel", self.is_overridable_at_agent_id_level)
        writer.write_object_value("teamworkConfiguration", self.teamwork_configuration)
    

