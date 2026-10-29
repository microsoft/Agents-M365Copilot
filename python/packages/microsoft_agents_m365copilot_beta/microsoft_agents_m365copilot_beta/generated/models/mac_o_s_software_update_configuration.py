from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_update_time_window import CustomUpdateTimeWindow
    from .device_configuration import DeviceConfiguration
    from .mac_o_s_priority import MacOSPriority
    from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
    from .mac_o_s_software_update_schedule_type import MacOSSoftwareUpdateScheduleType

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSSoftwareUpdateConfiguration(DeviceConfiguration, Parsable):
    """
    MacOS Software Update Configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSSoftwareUpdateConfiguration"
    # Update behavior options for macOS software updates.
    all_other_update_behavior: Optional[MacOSSoftwareUpdateBehavior] = None
    # Update behavior options for macOS software updates.
    config_data_update_behavior: Optional[MacOSSoftwareUpdateBehavior] = None
    # Update behavior options for macOS software updates.
    critical_update_behavior: Optional[MacOSSoftwareUpdateBehavior] = None
    # Custom Time windows when updates will be allowed or blocked. This collection can contain a maximum of 20 elements.
    custom_update_time_windows: Optional[list[CustomUpdateTimeWindow]] = None
    # Update behavior options for macOS software updates.
    firmware_update_behavior: Optional[MacOSSoftwareUpdateBehavior] = None
    # The maximum number of times the system allows the user to postpone an update before it’s installed. Supported values: 0 - 366. Valid values 0 to 365
    max_user_deferrals_count: Optional[int] = None
    # The scheduling priority for downloading and preparing the requested update. Default: Low. Possible values: Null, Low, High. Possible values are: low, high, unknownFutureValue.
    priority: Optional[MacOSPriority] = None
    # Update schedule type for macOS software updates.
    update_schedule_type: Optional[MacOSSoftwareUpdateScheduleType] = None
    # Minutes indicating UTC offset for each update time window
    update_time_window_utc_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSSoftwareUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSSoftwareUpdateConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_update_time_window import CustomUpdateTimeWindow
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_priority import MacOSPriority
        from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
        from .mac_o_s_software_update_schedule_type import MacOSSoftwareUpdateScheduleType

        from .custom_update_time_window import CustomUpdateTimeWindow
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_priority import MacOSPriority
        from .mac_o_s_software_update_behavior import MacOSSoftwareUpdateBehavior
        from .mac_o_s_software_update_schedule_type import MacOSSoftwareUpdateScheduleType

        fields: dict[str, Callable[[Any], None]] = {
            "allOtherUpdateBehavior": lambda n : setattr(self, 'all_other_update_behavior', n.get_enum_value(MacOSSoftwareUpdateBehavior)),
            "configDataUpdateBehavior": lambda n : setattr(self, 'config_data_update_behavior', n.get_enum_value(MacOSSoftwareUpdateBehavior)),
            "criticalUpdateBehavior": lambda n : setattr(self, 'critical_update_behavior', n.get_enum_value(MacOSSoftwareUpdateBehavior)),
            "customUpdateTimeWindows": lambda n : setattr(self, 'custom_update_time_windows', n.get_collection_of_object_values(CustomUpdateTimeWindow)),
            "firmwareUpdateBehavior": lambda n : setattr(self, 'firmware_update_behavior', n.get_enum_value(MacOSSoftwareUpdateBehavior)),
            "maxUserDeferralsCount": lambda n : setattr(self, 'max_user_deferrals_count', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(MacOSPriority)),
            "updateScheduleType": lambda n : setattr(self, 'update_schedule_type', n.get_enum_value(MacOSSoftwareUpdateScheduleType)),
            "updateTimeWindowUtcOffsetInMinutes": lambda n : setattr(self, 'update_time_window_utc_offset_in_minutes', n.get_int_value()),
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
        writer.write_enum_value("allOtherUpdateBehavior", self.all_other_update_behavior)
        writer.write_enum_value("configDataUpdateBehavior", self.config_data_update_behavior)
        writer.write_enum_value("criticalUpdateBehavior", self.critical_update_behavior)
        writer.write_collection_of_object_values("customUpdateTimeWindows", self.custom_update_time_windows)
        writer.write_enum_value("firmwareUpdateBehavior", self.firmware_update_behavior)
        writer.write_int_value("maxUserDeferralsCount", self.max_user_deferrals_count)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("updateScheduleType", self.update_schedule_type)
        writer.write_int_value("updateTimeWindowUtcOffsetInMinutes", self.update_time_window_utc_offset_in_minutes)
    

