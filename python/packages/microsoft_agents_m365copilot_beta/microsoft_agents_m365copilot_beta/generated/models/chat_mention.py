from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_mention_type import ChatMentionType

@dataclass
class ChatMention(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Character position of the mention within the message content.
    index: Optional[int] = None
    # Identifier of the mentioned user or application.
    mentioned: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of the mentioned entity. The possible values are: user, application, unknownFutureValue.
    type: Optional[ChatMentionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMention
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMention()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_mention_type import ChatMentionType

        from .chat_mention_type import ChatMentionType

        fields: dict[str, Callable[[Any], None]] = {
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "mentioned": lambda n : setattr(self, 'mentioned', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ChatMentionType)),
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
        writer.write_int_value("index", self.index)
        writer.write_str_value("mentioned", self.mentioned)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

