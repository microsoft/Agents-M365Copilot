from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.copilot_chat_response_options import CopilotChatResponseOptions
    from .....models.copilot_contextual_resources import CopilotContextualResources
    from .....models.copilot_context_message import CopilotContextMessage
    from .....models.copilot_conversation_location import CopilotConversationLocation
    from .....models.copilot_conversation_request_message_parameter import CopilotConversationRequestMessageParameter

@dataclass
class ChatPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The additionalContext property
    additional_context: Optional[list[CopilotContextMessage]] = None
    # Represents copilot contextual resources parameter.
    contextual_resources: Optional[CopilotContextualResources] = None
    # Represents a location.
    location_hint: Optional[CopilotConversationLocation] = None
    # The message property
    message: Optional[CopilotConversationRequestMessageParameter] = None
    # Represents copilot response options parameter.
    response_options: Optional[CopilotChatResponseOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.copilot_chat_response_options import CopilotChatResponseOptions
        from .....models.copilot_contextual_resources import CopilotContextualResources
        from .....models.copilot_context_message import CopilotContextMessage
        from .....models.copilot_conversation_location import CopilotConversationLocation
        from .....models.copilot_conversation_request_message_parameter import CopilotConversationRequestMessageParameter

        from .....models.copilot_chat_response_options import CopilotChatResponseOptions
        from .....models.copilot_contextual_resources import CopilotContextualResources
        from .....models.copilot_context_message import CopilotContextMessage
        from .....models.copilot_conversation_location import CopilotConversationLocation
        from .....models.copilot_conversation_request_message_parameter import CopilotConversationRequestMessageParameter

        fields: dict[str, Callable[[Any], None]] = {
            "additionalContext": lambda n : setattr(self, 'additional_context', n.get_collection_of_object_values(CopilotContextMessage)),
            "contextualResources": lambda n : setattr(self, 'contextual_resources', n.get_object_value(CopilotContextualResources)),
            "locationHint": lambda n : setattr(self, 'location_hint', n.get_object_value(CopilotConversationLocation)),
            "message": lambda n : setattr(self, 'message', n.get_object_value(CopilotConversationRequestMessageParameter)),
            "responseOptions": lambda n : setattr(self, 'response_options', n.get_object_value(CopilotChatResponseOptions)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("additionalContext", self.additional_context)
        writer.write_object_value("contextualResources", self.contextual_resources)
        writer.write_object_value("locationHint", self.location_hint)
        writer.write_object_value("message", self.message)
        writer.write_object_value("responseOptions", self.response_options)
        writer.write_additional_data_value(self.additional_data)
    

