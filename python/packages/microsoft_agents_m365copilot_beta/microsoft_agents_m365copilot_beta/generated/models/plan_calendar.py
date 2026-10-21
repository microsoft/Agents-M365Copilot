from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .work_day_defaults import WorkDayDefaults

@dataclass
class PlanCalendar(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Time zone the plan's calendar is expressed in.
    time_zone: Optional[str] = None
    # Default working-day start and end times for the plan.
    work_day_defaults: Optional[WorkDayDefaults] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlanCalendar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlanCalendar
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlanCalendar()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .work_day_defaults import WorkDayDefaults

        from .work_day_defaults import WorkDayDefaults

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "workDayDefaults": lambda n : setattr(self, 'work_day_defaults', n.get_object_value(WorkDayDefaults)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_object_value("workDayDefaults", self.work_day_defaults)
        writer.write_additional_data_value(self.additional_data)
    

