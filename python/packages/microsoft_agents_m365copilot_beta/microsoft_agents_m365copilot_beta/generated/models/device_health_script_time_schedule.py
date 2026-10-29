from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_health_script_daily_schedule import DeviceHealthScriptDailySchedule
    from .device_health_script_run_once_schedule import DeviceHealthScriptRunOnceSchedule
    from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

@dataclass
class DeviceHealthScriptTimeSchedule(DeviceHealthScriptRunSchedule, Parsable):
    """
    Base type of Device health script time schedule.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceHealthScriptTimeSchedule"
    # At what time the script is scheduled to run. This collection can contain a maximum of 20 elements.
    time: Optional[datetime.time] = None
    # Indicate if the time is Utc or client local time.
    use_utc: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptTimeSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptTimeSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptDailySchedule".casefold():
            from .device_health_script_daily_schedule import DeviceHealthScriptDailySchedule

            return DeviceHealthScriptDailySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceHealthScriptRunOnceSchedule".casefold():
            from .device_health_script_run_once_schedule import DeviceHealthScriptRunOnceSchedule

            return DeviceHealthScriptRunOnceSchedule()
        return DeviceHealthScriptTimeSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_health_script_daily_schedule import DeviceHealthScriptDailySchedule
        from .device_health_script_run_once_schedule import DeviceHealthScriptRunOnceSchedule
        from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

        from .device_health_script_daily_schedule import DeviceHealthScriptDailySchedule
        from .device_health_script_run_once_schedule import DeviceHealthScriptRunOnceSchedule
        from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "time": lambda n : setattr(self, 'time', n.get_time_value()),
            "useUtc": lambda n : setattr(self, 'use_utc', n.get_bool_value()),
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
        writer.write_time_value("time", self.time)
        writer.write_bool_value("useUtc", self.use_utc)
    

