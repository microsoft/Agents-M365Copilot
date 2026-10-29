from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .planner_task_chat_mention import PlannerTaskChatMention
    from .planner_task_chat_message_type import PlannerTaskChatMessageType
    from .planner_task_chat_reaction import PlannerTaskChatReaction

from .entity import Entity

@dataclass
class PlannerTaskChatMessage(Entity, Parsable):
    # The content of the chat message. Supports plain text and sanitized HTML.
    content: Optional[str] = None
    # The identity of the user who created the message.
    created_by: Optional[IdentitySet] = None
    # The date and time when the message was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The deletedDateTime property
    deleted_date_time: Optional[datetime.datetime] = None
    # The editedDateTime property
    edited_date_time: Optional[datetime.datetime] = None
    # The list of mentions in the message.
    mentions: Optional[list[PlannerTaskChatMention]] = None
    # The messageType property
    message_type: Optional[PlannerTaskChatMessageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the parent plannerTask that this message belongs to.
    parent_entity_id: Optional[str] = None
    # The reactions on the message.
    reactions: Optional[list[PlannerTaskChatReaction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskChatMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskChatMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskChatMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_task_chat_mention import PlannerTaskChatMention
        from .planner_task_chat_message_type import PlannerTaskChatMessageType
        from .planner_task_chat_reaction import PlannerTaskChatReaction

        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_task_chat_mention import PlannerTaskChatMention
        from .planner_task_chat_message_type import PlannerTaskChatMessageType
        from .planner_task_chat_reaction import PlannerTaskChatReaction

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "editedDateTime": lambda n : setattr(self, 'edited_date_time', n.get_datetime_value()),
            "mentions": lambda n : setattr(self, 'mentions', n.get_collection_of_object_values(PlannerTaskChatMention)),
            "messageType": lambda n : setattr(self, 'message_type', n.get_enum_value(PlannerTaskChatMessageType)),
            "parentEntityId": lambda n : setattr(self, 'parent_entity_id', n.get_str_value()),
            "reactions": lambda n : setattr(self, 'reactions', n.get_collection_of_object_values(PlannerTaskChatReaction)),
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
        writer.write_str_value("content", self.content)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_datetime_value("editedDateTime", self.edited_date_time)
        writer.write_collection_of_object_values("mentions", self.mentions)
        writer.write_enum_value("messageType", self.message_type)
        writer.write_str_value("parentEntityId", self.parent_entity_id)
        writer.write_collection_of_object_values("reactions", self.reactions)
    

