from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet

from .item_facet import ItemFacet

@dataclass
class PersonWebsite(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.personWebsite"
    # Contains categories a user has associated with the website (for example, personal, recipes).
    categories: Optional[list[str]] = None
    # Contains a description of the website.
    description: Optional[str] = None
    # Contains a friendly name for the website.
    display_name: Optional[str] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # Contains a link to the website itself.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersonWebsite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersonWebsite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersonWebsite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet

        from .item_facet import ItemFacet

        fields: dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    

