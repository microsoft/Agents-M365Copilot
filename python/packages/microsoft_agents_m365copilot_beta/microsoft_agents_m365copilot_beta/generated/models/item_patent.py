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
class ItemPatent(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.itemPatent"
    # Descpription of the patent or filing.
    description: Optional[str] = None
    # Title of the patent or filing.
    display_name: Optional[str] = None
    # Indicates the patent is pending.
    is_pending: Optional[bool] = None
    # The date that the patent was granted.
    issued_date: Optional[datetime.date] = None
    # Authority that granted the patent.
    issuing_authority: Optional[str] = None
    # The patent number.
    number: Optional[str] = None
    # URL referencing the patent or filing.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemPatent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPatent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemPatent()
    
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
            "isPending": lambda n : setattr(self, 'is_pending', n.get_bool_value()),
            "issuedDate": lambda n : setattr(self, 'issued_date', n.get_date_value()),
            "issuingAuthority": lambda n : setattr(self, 'issuing_authority', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
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
        writer.write_bool_value("isPending", self.is_pending)
        writer.write_date_value("issuedDate", self.issued_date)
        writer.write_str_value("issuingAuthority", self.issuing_authority)
        writer.write_str_value("number", self.number)
        writer.write_str_value("webUrl", self.web_url)
    

