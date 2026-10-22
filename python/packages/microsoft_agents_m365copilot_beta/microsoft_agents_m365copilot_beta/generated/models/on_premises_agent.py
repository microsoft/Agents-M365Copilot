from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_status import AgentStatus
    from .entity import Entity
    from .on_premises_agent_group import OnPremisesAgentGroup
    from .on_premises_publishing_type import OnPremisesPublishingType

from .entity import Entity

@dataclass
class OnPremisesAgent(Entity, Parsable):
    # List of onPremisesAgentGroups that an onPremisesAgent is assigned to. Read-only. Nullable.
    agent_groups: Optional[list[OnPremisesAgentGroup]] = None
    # The external IP address as detected by the service for the agent machine. Read-only
    external_ip: Optional[str] = None
    # The name of the machine that the agent is running on. Read-only
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[AgentStatus] = None
    # The possible values are: applicationProxy, exchangeOnline, authentication, provisioning, intunePfx, oflineDomainJoin, unknownFutureValue, privateAccess. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: privateAccess.
    supported_publishing_types: Optional[list[OnPremisesPublishingType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAgent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesAgent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_status import AgentStatus
        from .entity import Entity
        from .on_premises_agent_group import OnPremisesAgentGroup
        from .on_premises_publishing_type import OnPremisesPublishingType

        from .agent_status import AgentStatus
        from .entity import Entity
        from .on_premises_agent_group import OnPremisesAgentGroup
        from .on_premises_publishing_type import OnPremisesPublishingType

        fields: dict[str, Callable[[Any], None]] = {
            "agentGroups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(OnPremisesAgentGroup)),
            "externalIp": lambda n : setattr(self, 'external_ip', n.get_str_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AgentStatus)),
            "supportedPublishingTypes": lambda n : setattr(self, 'supported_publishing_types', n.get_collection_of_enum_values(OnPremisesPublishingType)),
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
        writer.write_collection_of_object_values("agentGroups", self.agent_groups)
        writer.write_str_value("externalIp", self.external_ip)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_enum_values("supportedPublishingTypes", self.supported_publishing_types)
    

