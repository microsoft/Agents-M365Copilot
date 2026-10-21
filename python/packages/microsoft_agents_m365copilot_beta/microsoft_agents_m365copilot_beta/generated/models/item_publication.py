from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet

from .item_facet import ItemFacet

@dataclass
class ItemPublication(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.itemPublication"
    # Description of the publication.
    description: Optional[str] = None
    # Title of the publication.
    display_name: Optional[str] = None
    # The date that the publication was published.
    published_date: Optional[datetime.date] = None
    # Publication or publisher for the publication.
    publisher: Optional[str] = None
    # URL referencing a thumbnail of the publication.
    thumbnail_url: Optional[str] = None
    # URL referencing the publication.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemPublication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPublication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemPublication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet

        from .item_facet import ItemFacet

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "publishedDate": lambda n : setattr(self, 'published_date', n.get_date_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("publishedDate", self.published_date)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    

