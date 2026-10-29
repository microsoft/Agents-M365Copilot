from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .year_reference_value import YearReferenceValue

from ..entity import Entity

@dataclass
class YearTimePeriodDefinition(Entity, Parsable):
    # The name of the year. Maximum supported length is 100 characters.
    display_name: Optional[str] = None
    # The last day of the year using ISO 8601 format for date.
    end_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The first day of the year using ISO 8601 format for date.
    start_date: Optional[datetime.date] = None
    # The year property
    year: Optional[YearReferenceValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> YearTimePeriodDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: YearTimePeriodDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return YearTimePeriodDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .year_reference_value import YearReferenceValue

        from ..entity import Entity
        from .year_reference_value import YearReferenceValue

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "year": lambda n : setattr(self, 'year', n.get_object_value(YearReferenceValue)),
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
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("startDate", self.start_date)
        writer.write_object_value("year", self.year)
    

