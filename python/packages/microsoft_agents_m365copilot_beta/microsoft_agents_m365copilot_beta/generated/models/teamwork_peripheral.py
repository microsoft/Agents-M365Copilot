from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class TeamworkPeripheral(Entity, Parsable):
    # Display name for the peripheral.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The product ID of the device. Each product from a vendor has its own ID.
    product_id: Optional[str] = None
    # The unique identifier for the vendor of the device. Each vendor has a unique ID.
    vendor_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkPeripheral:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheral
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkPeripheral()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "productId": lambda n : setattr(self, 'product_id', n.get_str_value()),
            "vendorId": lambda n : setattr(self, 'vendor_id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("productId", self.product_id)
        writer.write_str_value("vendorId", self.vendor_id)
    

