from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ItemActivityTimeSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The lastRecordedDateTime property
    last_recorded_date_time: Optional[datetime.datetime] = None
    # When the activity was observed to take place.
    observed_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When the observation was recorded on the service.
    recorded_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemActivityTimeSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityTimeSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemActivityTimeSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "lastRecordedDateTime": lambda n : setattr(self, 'last_recorded_date_time', n.get_datetime_value()),
            "observedDateTime": lambda n : setattr(self, 'observed_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recordedDateTime": lambda n : setattr(self, 'recorded_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("lastRecordedDateTime", self.last_recorded_date_time)
        writer.write_datetime_value("observedDateTime", self.observed_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("recordedDateTime", self.recorded_date_time)
        writer.write_additional_data_value(self.additional_data)
    

