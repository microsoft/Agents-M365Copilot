from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class AgentRegistration(Entity, Parsable):
    """
    Entity that represents an agent registration containing metadata, endpointconfiguration, tools, and publishing information.This entity provides developers and administrators with all details needed tomanage agent instances including their instructions, owners, publishing status,and associated tools.
    """
    # Agent identity blueprint identifier.
    agent_identity_blueprint_id: Optional[str] = None
    # Entra agent identity identifier.
    agent_identity_id: Optional[str] = None
    # The unique identifier of the user or app who created the agent registration.
    created_by: Optional[str] = None
    # The agent description providing an overview of its purpose and capabilities.
    description: Optional[str] = None
    # Display name for the agent instance.
    display_name: Optional[str] = None
    # The unique identifier of the last person to publish the agent.
    last_published_by: Optional[str] = None
    # Application identifier managing this agent.
    managed_by_app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the store/system where the agent originated.
    originating_store: Optional[str] = None
    # List of owner identifiers  for the agent in case of user registering agent. Either owners or managedby is required
    owner_ids: Optional[list[str]] = None
    # Original agent identifier from source system.
    source_agent_id: Optional[str] = None
    # The date and time when the agent instance was created from source.
    source_created_date_time: Optional[datetime.datetime] = None
    # The date and time when the agent instance was last modified from source.
    source_last_modified_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentRegistration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentRegistration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "agentIdentityBlueprintId": lambda n : setattr(self, 'agent_identity_blueprint_id', n.get_str_value()),
            "agentIdentityId": lambda n : setattr(self, 'agent_identity_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastPublishedBy": lambda n : setattr(self, 'last_published_by', n.get_str_value()),
            "managedByAppId": lambda n : setattr(self, 'managed_by_app_id', n.get_str_value()),
            "originatingStore": lambda n : setattr(self, 'originating_store', n.get_str_value()),
            "ownerIds": lambda n : setattr(self, 'owner_ids', n.get_collection_of_primitive_values(str)),
            "sourceAgentId": lambda n : setattr(self, 'source_agent_id', n.get_str_value()),
            "sourceCreatedDateTime": lambda n : setattr(self, 'source_created_date_time', n.get_datetime_value()),
            "sourceLastModifiedDateTime": lambda n : setattr(self, 'source_last_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("agentIdentityBlueprintId", self.agent_identity_blueprint_id)
        writer.write_str_value("agentIdentityId", self.agent_identity_id)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastPublishedBy", self.last_published_by)
        writer.write_str_value("managedByAppId", self.managed_by_app_id)
        writer.write_str_value("originatingStore", self.originating_store)
        writer.write_collection_of_primitive_values("ownerIds", self.owner_ids)
        writer.write_str_value("sourceAgentId", self.source_agent_id)
        writer.write_datetime_value("sourceCreatedDateTime", self.source_created_date_time)
        writer.write_datetime_value("sourceLastModifiedDateTime", self.source_last_modified_date_time)
    

