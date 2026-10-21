from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add_footer import AddFooter
    from .add_header import AddHeader
    from .add_watermark import AddWatermark
    from .label_action_base import LabelActionBase

from .label_action_base import LabelActionBase

@dataclass
class MarkContent(LabelActionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.markContent"
    # The fontColor property
    font_color: Optional[str] = None
    # The fontSize property
    font_size: Optional[int] = None
    # The text property
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MarkContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MarkContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addFooter".casefold():
            from .add_footer import AddFooter

            return AddFooter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addHeader".casefold():
            from .add_header import AddHeader

            return AddHeader()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addWatermark".casefold():
            from .add_watermark import AddWatermark

            return AddWatermark()
        return MarkContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .add_footer import AddFooter
        from .add_header import AddHeader
        from .add_watermark import AddWatermark
        from .label_action_base import LabelActionBase

        from .add_footer import AddFooter
        from .add_header import AddHeader
        from .add_watermark import AddWatermark
        from .label_action_base import LabelActionBase

        fields: dict[str, Callable[[Any], None]] = {
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "fontSize": lambda n : setattr(self, 'font_size', n.get_int_value()),
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
        writer.write_str_value("fontColor", self.font_color)
        writer.write_int_value("fontSize", self.font_size)
        writer.write_str_value("text", self.text)
    

