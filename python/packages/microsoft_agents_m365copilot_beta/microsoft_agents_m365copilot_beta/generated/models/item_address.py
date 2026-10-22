from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .geo_coordinates import GeoCoordinates
    from .item_facet import ItemFacet
    from .physical_address import PhysicalAddress

from .item_facet import ItemFacet

@dataclass
class ItemAddress(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.itemAddress"
    # Details about the address itself.
    detail: Optional[PhysicalAddress] = None
    # Friendly name the user has assigned to this address.
    display_name: Optional[str] = None
    # The geocoordinates of the address.
    geo_coordinates: Optional[GeoCoordinates] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .geo_coordinates import GeoCoordinates
        from .item_facet import ItemFacet
        from .physical_address import PhysicalAddress

        from .geo_coordinates import GeoCoordinates
        from .item_facet import ItemFacet
        from .physical_address import PhysicalAddress

        fields: dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(PhysicalAddress)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(GeoCoordinates)),
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
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
    

