from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_citation_sensitivity_label import ChatMessageCitationSensitivityLabel

@dataclass
class ChatMessageCitation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Read-only. Text snippet from the cited source.
    excerpt: Optional[str] = None
    # Read-only. Icon type identifier for the cited source, for example, ExcelIcon or WordIcon.
    icon_type: Optional[str] = None
    # Read-only. Citation identifier that's unique within the message. The message body references this identifier inline, for example, [1].
    id: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Sensitivity label applied to the cited source.
    sensitivity_label: Optional[ChatMessageCitationSensitivityLabel] = None
    # Read-only. Display title of the cited source.
    title: Optional[str] = None
    # Read-only. URL to the cited source.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMessageCitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageCitation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMessageCitation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_citation_sensitivity_label import ChatMessageCitationSensitivityLabel

        from .chat_message_citation_sensitivity_label import ChatMessageCitationSensitivityLabel

        fields: dict[str, Callable[[Any], None]] = {
            "excerpt": lambda n : setattr(self, 'excerpt', n.get_str_value()),
            "iconType": lambda n : setattr(self, 'icon_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitivityLabel": lambda n : setattr(self, 'sensitivity_label', n.get_object_value(ChatMessageCitationSensitivityLabel)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("excerpt", self.excerpt)
        writer.write_str_value("iconType", self.icon_type)
        writer.write_int_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sensitivityLabel", self.sensitivity_label)
        writer.write_str_value("title", self.title)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    

