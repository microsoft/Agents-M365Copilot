from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_card_manifest import AgentCardManifest
    from .agent_card_signature import AgentCardSignature
    from .agent_collection import AgentCollection
    from .agent_interface import AgentInterface
    from .entity import Entity

from .entity import Entity

@dataclass
class AgentInstance(Entity, Parsable):
    # Additional interfaces/transports supported by the agent.
    additional_interfaces: Optional[list[AgentInterface]] = None
    # The agent card manifest of the agent instance.
    agent_card_manifest: Optional[AgentCardManifest] = None
    # Object ID of the agentIdentityBlueprint object.
    agent_identity_blueprint_id: Optional[str] = None
    # Object ID of the agentIdentity object.
    agent_identity_id: Optional[str] = None
    # Object ID of the agentUser associated with the agent. Read-only.
    agent_user_id: Optional[str] = None
    # The agent collections that the agent instance is a member of.
    collections: Optional[list[AgentCollection]] = None
    # Object ID of the user or application that created the agent instance. Read-only.
    created_by: Optional[str] = None
    # Timestamp when agent instance was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Display name for the agent instance.
    display_name: Optional[str] = None
    # Timestamp of last modification.
    last_modified_date_time: Optional[datetime.datetime] = None
    # appId (referred to as Application (client) ID on the Microsoft Entra admin center) of the application managing this agent.
    managed_by: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the store/system where agent originated. For example Copilot Studio.
    originating_store: Optional[str] = None
    # List of object IDs for the owners of the agent instance.
    owner_ids: Optional[list[str]] = None
    # Preferred transport protocol. The possible values are JSONRPC, GRPC, and HTTP+JSON.
    preferred_transport: Optional[str] = None
    # Digital signatures for the agent instance.
    signatures: Optional[list[AgentCardSignature]] = None
    # Identifier of the agent in the original source system.
    source_agent_id: Optional[str] = None
    # Endpoint URL for the agent instance.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_card_manifest import AgentCardManifest
        from .agent_card_signature import AgentCardSignature
        from .agent_collection import AgentCollection
        from .agent_interface import AgentInterface
        from .entity import Entity

        from .agent_card_manifest import AgentCardManifest
        from .agent_card_signature import AgentCardSignature
        from .agent_collection import AgentCollection
        from .agent_interface import AgentInterface
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInterfaces": lambda n : setattr(self, 'additional_interfaces', n.get_collection_of_object_values(AgentInterface)),
            "agentCardManifest": lambda n : setattr(self, 'agent_card_manifest', n.get_object_value(AgentCardManifest)),
            "agentIdentityBlueprintId": lambda n : setattr(self, 'agent_identity_blueprint_id', n.get_str_value()),
            "agentIdentityId": lambda n : setattr(self, 'agent_identity_id', n.get_str_value()),
            "agentUserId": lambda n : setattr(self, 'agent_user_id', n.get_str_value()),
            "collections": lambda n : setattr(self, 'collections', n.get_collection_of_object_values(AgentCollection)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "originatingStore": lambda n : setattr(self, 'originating_store', n.get_str_value()),
            "ownerIds": lambda n : setattr(self, 'owner_ids', n.get_collection_of_primitive_values(str)),
            "preferredTransport": lambda n : setattr(self, 'preferred_transport', n.get_str_value()),
            "signatures": lambda n : setattr(self, 'signatures', n.get_collection_of_object_values(AgentCardSignature)),
            "sourceAgentId": lambda n : setattr(self, 'source_agent_id', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_collection_of_object_values("additionalInterfaces", self.additional_interfaces)
        writer.write_object_value("agentCardManifest", self.agent_card_manifest)
        writer.write_str_value("agentIdentityBlueprintId", self.agent_identity_blueprint_id)
        writer.write_str_value("agentIdentityId", self.agent_identity_id)
        writer.write_str_value("agentUserId", self.agent_user_id)
        writer.write_collection_of_object_values("collections", self.collections)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_str_value("originatingStore", self.originating_store)
        writer.write_collection_of_primitive_values("ownerIds", self.owner_ids)
        writer.write_str_value("preferredTransport", self.preferred_transport)
        writer.write_collection_of_object_values("signatures", self.signatures)
        writer.write_str_value("sourceAgentId", self.source_agent_id)
        writer.write_str_value("url", self.url)
    

