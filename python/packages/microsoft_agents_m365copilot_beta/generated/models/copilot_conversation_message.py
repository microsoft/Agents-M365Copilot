from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_conversation_request_message import CopilotConversationRequestMessage
    from .copilot_conversation_response_message import CopilotConversationResponseMessage
    from .entity import Entity

from .entity import Entity

@dataclass
class CopilotConversationMessage(Entity, Parsable):
    """
    Abstract entity representing a chat message in a request or response.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The text of the message.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotConversationMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotConversationMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotConversationRequestMessage".casefold():
            from .copilot_conversation_request_message import CopilotConversationRequestMessage

            return CopilotConversationRequestMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotConversationResponseMessage".casefold():
            from .copilot_conversation_response_message import CopilotConversationResponseMessage

            return CopilotConversationResponseMessage()
        return CopilotConversationMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_conversation_request_message import CopilotConversationRequestMessage
        from .copilot_conversation_response_message import CopilotConversationResponseMessage
        from .entity import Entity

        from .copilot_conversation_request_message import CopilotConversationRequestMessage
        from .copilot_conversation_response_message import CopilotConversationResponseMessage
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("text", self.text)
    

