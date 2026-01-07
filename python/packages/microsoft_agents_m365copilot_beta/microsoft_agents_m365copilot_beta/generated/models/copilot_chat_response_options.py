from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CopilotChatResponseOptions(AdditionalDataHolder, Parsable):
    """
    Represents copilot response options parameter.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether adaptive cards are enabled in the response.
    is_adaptive_card_enabled: Optional[bool] = None
    # Indicates whether annotations are enabled in the response.
    is_annotations_enabled: Optional[bool] = None
    # Indicates whether delta streaming is enabled in the response.
    is_delta_streaming_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotChatResponseOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotChatResponseOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotChatResponseOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isAdaptiveCardEnabled": lambda n : setattr(self, 'is_adaptive_card_enabled', n.get_bool_value()),
            "isAnnotationsEnabled": lambda n : setattr(self, 'is_annotations_enabled', n.get_bool_value()),
            "isDeltaStreamingEnabled": lambda n : setattr(self, 'is_delta_streaming_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isAdaptiveCardEnabled", self.is_adaptive_card_enabled)
        writer.write_bool_value("isAnnotationsEnabled", self.is_annotations_enabled)
        writer.write_bool_value("isDeltaStreamingEnabled", self.is_delta_streaming_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

