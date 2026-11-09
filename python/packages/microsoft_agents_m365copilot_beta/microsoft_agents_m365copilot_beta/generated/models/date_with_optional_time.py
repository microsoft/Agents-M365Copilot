from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DateWithOptionalTime(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date component of the value.
    date: Optional[datetime.date] = None
    # Indicates whether a specific time (not just a date) was provided.
    is_time_specified: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The optional time-of-day component of the value.
    time: Optional[datetime.time] = None
    # Time zone the time value is expressed in, if time is set.
    time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DateWithOptionalTime:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DateWithOptionalTime
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DateWithOptionalTime()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "isTimeSpecified": lambda n : setattr(self, 'is_time_specified', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time": lambda n : setattr(self, 'time', n.get_time_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_date_value("date", self.date)
        writer.write_bool_value("isTimeSpecified", self.is_time_specified)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("time", self.time)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    

