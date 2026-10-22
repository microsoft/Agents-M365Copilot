from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AccessReviewRecurrenceSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The duration in days for recurrence.
    duration_in_days: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The count of recurrences, if the value of recurrenceEndType is occurrences, or 0 otherwise.
    recurrence_count: Optional[int] = None
    # How the recurrence ends. Possible values: never, endBy, occurrences, or recurrenceCount. If it's never, then there's no explicit end of the recurrence series. If it's endBy, then the recurrence ends at a certain date. If it's occurrences, then the series ends after recurrenceCount instances of the review have completed.
    recurrence_end_type: Optional[str] = None
    # The recurrence interval. Possible values: onetime, weekly, monthly, quarterly, halfyearly or annual.
    recurrence_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewRecurrenceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewRecurrenceSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewRecurrenceSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrenceCount": lambda n : setattr(self, 'recurrence_count', n.get_int_value()),
            "recurrenceEndType": lambda n : setattr(self, 'recurrence_end_type', n.get_str_value()),
            "recurrenceType": lambda n : setattr(self, 'recurrence_type', n.get_str_value()),
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
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("recurrenceCount", self.recurrence_count)
        writer.write_str_value("recurrenceEndType", self.recurrence_end_type)
        writer.write_str_value("recurrenceType", self.recurrence_type)
        writer.write_additional_data_value(self.additional_data)
    

