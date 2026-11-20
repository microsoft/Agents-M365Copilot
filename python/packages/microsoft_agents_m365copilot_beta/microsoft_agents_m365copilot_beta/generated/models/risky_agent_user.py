from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_user import AgentUser
    from .risky_agent import RiskyAgent

from .risky_agent import RiskyAgent

@dataclass
class RiskyAgentUser(RiskyAgent, Parsable):
    # The agentUser property
    agent_user: Optional[AgentUser] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskyAgentUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskyAgentUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskyAgentUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_user import AgentUser
        from .risky_agent import RiskyAgent

        from .agent_user import AgentUser
        from .risky_agent import RiskyAgent

        fields: dict[str, Callable[[Any], None]] = {
            "agentUser": lambda n : setattr(self, 'agent_user', n.get_object_value(AgentUser)),
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
        writer.write_object_value("agentUser", self.agent_user)
    

