from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_site_page import BaseSitePage
    from .canvas_layout import CanvasLayout
    from .title_area import TitleArea
    from .web_part import WebPart

from .base_site_page import BaseSitePage

@dataclass
class PageTemplate(BaseSitePage, Parsable):
    # The layout of the content in a given SharePoint page template, including horizontal sections and vertical sections.
    canvas_layout: Optional[CanvasLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The title area on the SharePoint page template.
    title_area: Optional[TitleArea] = None
    # The collection of web parts on the SharePoint page.
    web_parts: Optional[list[WebPart]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PageTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PageTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PageTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_site_page import BaseSitePage
        from .canvas_layout import CanvasLayout
        from .title_area import TitleArea
        from .web_part import WebPart

        from .base_site_page import BaseSitePage
        from .canvas_layout import CanvasLayout
        from .title_area import TitleArea
        from .web_part import WebPart

        fields: dict[str, Callable[[Any], None]] = {
            "canvasLayout": lambda n : setattr(self, 'canvas_layout', n.get_object_value(CanvasLayout)),
            "titleArea": lambda n : setattr(self, 'title_area', n.get_object_value(TitleArea)),
            "webParts": lambda n : setattr(self, 'web_parts', n.get_collection_of_object_values(WebPart)),
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
        writer.write_object_value("canvasLayout", self.canvas_layout)
        writer.write_object_value("titleArea", self.title_area)
        writer.write_collection_of_object_values("webParts", self.web_parts)
    

