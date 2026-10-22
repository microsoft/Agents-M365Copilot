from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_properties import ChatMessageProperties
    from .identity_set import IdentitySet
    from .planner_chat_message_type import PlannerChatMessageType
    from .planner_chat_thread_type import PlannerChatThreadType
    from .planner_delta import PlannerDelta

from .planner_delta import PlannerDelta

@dataclass
class PlannerChatMessage(PlannerDelta, Parsable):
    # Body content of the chat message.
    content: Optional[str] = None
    # Identity of the user (or application) who created the entity. Read-only.
    created_by: Optional[IdentitySet] = None
    # Date and time the entity was created. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Date and time the message was deleted.
    deleted_time: Optional[datetime.datetime] = None
    # Date and time the message was last edited.
    edited_time: Optional[datetime.datetime] = None
    # Indicates whether the message was deleted.
    is_deleted: Optional[bool] = None
    # Indicates whether the message was edited after it was sent.
    is_edited: Optional[bool] = None
    # Format of the message content. The possible values are: richTextHtml, plainText, unknownFutureValue.
    message_type: Optional[PlannerChatMessageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the task or plan the message belongs to.
    parent_entity_id: Optional[str] = None
    # @mentions and reactions associated with the message.
    properties: Optional[ChatMessageProperties] = None
    # Indicates whether the message belongs to a task-level or plan-level conversation. The possible values are: task, plan, unknownFutureValue.
    thread_type: Optional[PlannerChatThreadType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerChatMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerChatMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerChatMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_properties import ChatMessageProperties
        from .identity_set import IdentitySet
        from .planner_chat_message_type import PlannerChatMessageType
        from .planner_chat_thread_type import PlannerChatThreadType
        from .planner_delta import PlannerDelta

        from .chat_message_properties import ChatMessageProperties
        from .identity_set import IdentitySet
        from .planner_chat_message_type import PlannerChatMessageType
        from .planner_chat_thread_type import PlannerChatThreadType
        from .planner_delta import PlannerDelta

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedTime": lambda n : setattr(self, 'deleted_time', n.get_datetime_value()),
            "editedTime": lambda n : setattr(self, 'edited_time', n.get_datetime_value()),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "isEdited": lambda n : setattr(self, 'is_edited', n.get_bool_value()),
            "messageType": lambda n : setattr(self, 'message_type', n.get_enum_value(PlannerChatMessageType)),
            "parentEntityId": lambda n : setattr(self, 'parent_entity_id', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(ChatMessageProperties)),
            "threadType": lambda n : setattr(self, 'thread_type', n.get_enum_value(PlannerChatThreadType)),
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
        writer.write_datetime_value("deletedTime", self.deleted_time)
        writer.write_datetime_value("editedTime", self.edited_time)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_bool_value("isEdited", self.is_edited)
        writer.write_enum_value("messageType", self.message_type)
        writer.write_str_value("parentEntityId", self.parent_entity_id)
        writer.write_object_value("properties", self.properties)
        writer.write_enum_value("threadType", self.thread_type)
    

