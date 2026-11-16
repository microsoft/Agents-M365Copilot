from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet
    from .person_annual_event_type import PersonAnnualEventType

from .item_facet import ItemFacet

@dataclass
class PersonAnnualEvent(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.personAnnualEvent"
    # The date property
    date: Optional[datetime.date] = None
    # The displayName property
    display_name: Optional[str] = None
    # The type property
    type: Optional[PersonAnnualEventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersonAnnualEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersonAnnualEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersonAnnualEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet
        from .person_annual_event_type import PersonAnnualEventType

        from .item_facet import ItemFacet
        from .person_annual_event_type import PersonAnnualEventType

        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PersonAnnualEventType)),
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
        writer.write_date_value("date", self.date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("type", self.type)
    

