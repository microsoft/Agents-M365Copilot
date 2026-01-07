from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_conversation_attribution import CopilotConversationAttribution
    from .copilot_conversation_message import CopilotConversationMessage
    from .json import Json
    from .search_sensitivity_label_info import SearchSensitivityLabelInfo

from .copilot_conversation_message import CopilotConversationMessage

@dataclass
class CopilotConversationResponseMessage(CopilotConversationMessage, Parsable):
    """
    Represents a response message in a chat.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.copilotConversationResponseMessage"
    # The adaptiveCards property
    adaptive_cards: Optional[list[Json]] = None
    # The attributions property
    attributions: Optional[list[CopilotConversationAttribution]] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The sensitivityLabel property
    sensitivity_label: Optional[SearchSensitivityLabelInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotConversationResponseMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotConversationResponseMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotConversationResponseMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_conversation_attribution import CopilotConversationAttribution
        from .copilot_conversation_message import CopilotConversationMessage
        from .json import Json
        from .search_sensitivity_label_info import SearchSensitivityLabelInfo

        from .copilot_conversation_attribution import CopilotConversationAttribution
        from .copilot_conversation_message import CopilotConversationMessage
        from .json import Json
        from .search_sensitivity_label_info import SearchSensitivityLabelInfo

        fields: dict[str, Callable[[Any], None]] = {
            "adaptiveCards": lambda n : setattr(self, 'adaptive_cards', n.get_collection_of_object_values(Json)),
            "attributions": lambda n : setattr(self, 'attributions', n.get_collection_of_object_values(CopilotConversationAttribution)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "sensitivityLabel": lambda n : setattr(self, 'sensitivity_label', n.get_object_value(SearchSensitivityLabelInfo)),
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
    

