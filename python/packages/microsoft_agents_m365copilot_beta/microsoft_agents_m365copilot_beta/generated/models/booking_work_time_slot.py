from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BookingWorkTimeSlot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The time of the day when work stops. For example, 17:00:00.0000000.
    end: Optional[datetime.time] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time of the day when work starts. For example, 08:00:00.0000000.
    start: Optional[datetime.time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingWorkTimeSlot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingWorkTimeSlot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingWorkTimeSlot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "end": lambda n : setattr(self, 'end', n.get_time_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_time_value()),
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
        writer.write_time_value("end", self.end)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("start", self.start)
        writer.write_additional_data_value(self.additional_data)
    

