from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RuleSchedule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The recurring time interval at which the rule runs (ISO 8601 duration, for example P1D for daily, PT1H for hourly).
    frequency: Optional[datetime.timedelta] = None
    # Timestamp of the custom detection rule's next scheduled run. Deprecated. This property will be removed from this resource on 2026-10-01.
    next_run_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # How often the detection rule is set to run. The allowed values are: 0, 1H, 3H, 12H, or 24H. 0 signifies the rule is run continuously. Deprecated. Use frequency instead. This property will be removed from this resource on 2026-10-01.
    period: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RuleSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RuleSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RuleSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "frequency": lambda n : setattr(self, 'frequency', n.get_timedelta_value()),
            "nextRunDateTime": lambda n : setattr(self, 'next_run_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "period": lambda n : setattr(self, 'period', n.get_str_value()),
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
        writer.write_timedelta_value("frequency", self.frequency)
        writer.write_datetime_value("nextRunDateTime", self.next_run_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("period", self.period)
        writer.write_additional_data_value(self.additional_data)
    

