from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_conversation_message import CopilotConversationMessage
    from .copilot_conversation_state import CopilotConversationState
    from .entity import Entity

from .entity import Entity

@dataclass
class CopilotConversation(Entity, Parsable):
    """
    Conversation is a first class object in the system, and consists of persistent metadata plus a stream of messages,typically alternating request/response, implicitly forming a turn.Represents a conversation with Copilot Chat.
    """
    # The date and time when the conversation was created.
    created_date_time: Optional[datetime.datetime] = None
    # The display name of the conversation.
    display_name: Optional[str] = None
    # The ordered list of messages in the conversation.
    messages: Optional[list[CopilotConversationMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of a Copilot conversation.
    state: Optional[CopilotConversationState] = None
    # The number of turns in the conversation.
    turn_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotConversation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotConversation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotConversation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_conversation_message import CopilotConversationMessage
        from .copilot_conversation_state import CopilotConversationState
        from .entity import Entity

        from .copilot_conversation_message import CopilotConversationMessage
        from .copilot_conversation_state import CopilotConversationState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(CopilotConversationMessage)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(CopilotConversationState)),
            "turnCount": lambda n : setattr(self, 'turn_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_enum_value("state", self.state)
    

