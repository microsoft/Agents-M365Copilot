from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .item_facet import ItemFacet

from .item_facet import ItemFacet

@dataclass
class PersonAnnotation(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.personAnnotation"
    # Contains the detail of the note itself.
    detail: Optional[ItemBody] = None
    # Contains a friendly name for the note.
    display_name: Optional[str] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersonAnnotation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersonAnnotation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersonAnnotation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .item_facet import ItemFacet

        from .item_body import ItemBody
        from .item_facet import ItemFacet

        fields: dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(ItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
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
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
    

