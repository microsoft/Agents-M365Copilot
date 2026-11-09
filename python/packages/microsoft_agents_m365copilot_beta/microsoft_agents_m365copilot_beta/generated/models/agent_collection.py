from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_instance import AgentInstance
    from .entity import Entity

from .entity import Entity

@dataclass
class AgentCollection(Entity, Parsable):
    # Object ID of the user or app that created the agent instance.
    created_by: Optional[str] = None
    # Timestamp when agent collection was created.
    created_date_time: Optional[datetime.datetime] = None
    # Description / purpose of the collection.
    description: Optional[str] = None
    # Friendly name of the collection.
    display_name: Optional[str] = None
    # Timestamp of last update.
    last_modified_date_time: Optional[datetime.datetime] = None
    # appId (referred to as Application (client) ID on the Microsoft Entra admin center) of the service principal managing this agent.
    managed_by: Optional[str] = None
    # List of agent instances that are members of this collection. Supports $expand.
    members: Optional[list[AgentInstance]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Source system/store where the collection originated. For example Copilot Studio.
    originating_store: Optional[str] = None
    # List of object IDs for the owners of the agent instance.
    owner_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentCollection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentCollection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_instance import AgentInstance
        from .entity import Entity

        from .agent_instance import AgentInstance
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(AgentInstance)),
            "originatingStore": lambda n : setattr(self, 'originating_store', n.get_str_value()),
            "ownerIds": lambda n : setattr(self, 'owner_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("originatingStore", self.originating_store)
        writer.write_collection_of_primitive_values("ownerIds", self.owner_ids)
    

