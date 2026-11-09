from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_conversation_configuration import AgentConversationConfiguration

@dataclass
class AgentTeamworkConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The message notification settings that the agent uses in channels.
    channel_configuration: Optional[AgentConversationConfiguration] = None
    # The message notification settings that the agent uses in group chats.
    group_chat_configuration: Optional[AgentConversationConfiguration] = None
    # The message notification settings that the agent uses in meeting chats.
    meeting_chat_configuration: Optional[AgentConversationConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The message notification settings that the agent uses in one-on-one chats.
    one_on_one_chat_configuration: Optional[AgentConversationConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentTeamworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentTeamworkConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentTeamworkConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_conversation_configuration import AgentConversationConfiguration

        from .agent_conversation_configuration import AgentConversationConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "channelConfiguration": lambda n : setattr(self, 'channel_configuration', n.get_object_value(AgentConversationConfiguration)),
            "groupChatConfiguration": lambda n : setattr(self, 'group_chat_configuration', n.get_object_value(AgentConversationConfiguration)),
            "meetingChatConfiguration": lambda n : setattr(self, 'meeting_chat_configuration', n.get_object_value(AgentConversationConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oneOnOneChatConfiguration": lambda n : setattr(self, 'one_on_one_chat_configuration', n.get_object_value(AgentConversationConfiguration)),
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
        writer.write_object_value("channelConfiguration", self.channel_configuration)
        writer.write_object_value("groupChatConfiguration", self.group_chat_configuration)
        writer.write_object_value("meetingChatConfiguration", self.meeting_chat_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("oneOnOneChatConfiguration", self.one_on_one_chat_configuration)
        writer.write_additional_data_value(self.additional_data)
    

