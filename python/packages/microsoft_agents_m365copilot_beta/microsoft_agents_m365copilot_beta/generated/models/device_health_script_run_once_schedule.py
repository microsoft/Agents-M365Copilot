from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_health_script_time_schedule import DeviceHealthScriptTimeSchedule

from .device_health_script_time_schedule import DeviceHealthScriptTimeSchedule

@dataclass
class DeviceHealthScriptRunOnceSchedule(DeviceHealthScriptTimeSchedule, Parsable):
    """
    Device health script run once schedule.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceHealthScriptRunOnceSchedule"
    # The date the script is scheduled to run. This collection can contain a maximum of 20 elements.
    date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptRunOnceSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRunOnceSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptRunOnceSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_health_script_time_schedule import DeviceHealthScriptTimeSchedule

        from .device_health_script_time_schedule import DeviceHealthScriptTimeSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
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
    

