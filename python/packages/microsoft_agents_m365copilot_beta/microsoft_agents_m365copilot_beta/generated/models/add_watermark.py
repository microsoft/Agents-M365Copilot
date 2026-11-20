from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mark_content import MarkContent
    from .page_orientation import PageOrientation

from .mark_content import MarkContent

@dataclass
class AddWatermark(MarkContent, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.addWatermark"
    # The orientation property
    orientation: Optional[PageOrientation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AddWatermark:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddWatermark
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AddWatermark()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mark_content import MarkContent
        from .page_orientation import PageOrientation

        from .mark_content import MarkContent
        from .page_orientation import PageOrientation

        fields: dict[str, Callable[[Any], None]] = {
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(PageOrientation)),
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
        writer.write_enum_value("orientation", self.orientation)
    

