from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_device_battery_detail import UserExperienceAnalyticsDeviceBatteryDetail
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBatteryHealthDevicePerformance(Entity, Parsable):
    """
    The user experience analytics battery health device performance entity contains device level battery information.
    """
    # Estimated battery age. Unit in days. Valid values 0 to 2147483647
    battery_age_in_days: Optional[int] = None
    # Properties (maxCapacity and cycleCount) related to all batteries of the device.
    device_batteries_details: Optional[list[UserExperienceAnalyticsDeviceBatteryDetail]] = None
    # Number of batteries in a user device. Valid values 0 to 2147483647
    device_battery_count: Optional[int] = None
    # A weighted average of a device’s maximum capacity score and runtime estimate score. Values range from 0-100. Valid values 0 to 2147483647
    device_battery_health_score: Optional[int] = None
    # Tags for computed information on how battery on the device is behaving. E.g. newbattery, batterycapacityred, designcapacityzero, etc.
    device_battery_tags: Optional[list[str]] = None
    # The unique identifier of the device, Intune DeviceID.
    device_id: Optional[str] = None
    # The manufacturer name of the device.
    device_manufacturer_name: Optional[str] = None
    # The model name of the device.
    device_model_name: Optional[str] = None
    # Device friendly name.
    device_name: Optional[str] = None
    # The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values 0 to 2147483647
    estimated_runtime_in_minutes: Optional[int] = None
    # Number of times the battery has been discharged an amount that equals 100% of its capacity, but not necessarily by discharging it from 100% to 0%. Valid values 0 to 2147483647
    full_battery_drain_count: Optional[int] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # The manufacturer name of the device. Deprecated in favor of DeviceManufacturerName.
    manufacturer: Optional[str] = None
    # Ratio of current capacity and design capacity of the battery with the lowest capacity. Unit in percentage and values range from 0-100. Valid values 0 to 2147483647
    max_capacity_percentage: Optional[int] = None
    # The model name of the device. Deprecated in favor of DeviceModelName.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsBatteryHealthDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthDevicePerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthDevicePerformance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_device_battery_detail import UserExperienceAnalyticsDeviceBatteryDetail
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        from .entity import Entity
        from .user_experience_analytics_device_battery_detail import UserExperienceAnalyticsDeviceBatteryDetail
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        fields: dict[str, Callable[[Any], None]] = {
            "batteryAgeInDays": lambda n : setattr(self, 'battery_age_in_days', n.get_int_value()),
            "deviceBatteriesDetails": lambda n : setattr(self, 'device_batteries_details', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceBatteryDetail)),
            "deviceBatteryCount": lambda n : setattr(self, 'device_battery_count', n.get_int_value()),
            "deviceBatteryHealthScore": lambda n : setattr(self, 'device_battery_health_score', n.get_int_value()),
            "deviceBatteryTags": lambda n : setattr(self, 'device_battery_tags', n.get_collection_of_primitive_values(str)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceManufacturerName": lambda n : setattr(self, 'device_manufacturer_name', n.get_str_value()),
            "deviceModelName": lambda n : setattr(self, 'device_model_name', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "estimatedRuntimeInMinutes": lambda n : setattr(self, 'estimated_runtime_in_minutes', n.get_int_value()),
            "fullBatteryDrainCount": lambda n : setattr(self, 'full_battery_drain_count', n.get_int_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "maxCapacityPercentage": lambda n : setattr(self, 'max_capacity_percentage', n.get_int_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
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
        writer.write_int_value("batteryAgeInDays", self.battery_age_in_days)
        writer.write_collection_of_object_values("deviceBatteriesDetails", self.device_batteries_details)
        writer.write_int_value("deviceBatteryCount", self.device_battery_count)
        writer.write_int_value("deviceBatteryHealthScore", self.device_battery_health_score)
        writer.write_collection_of_primitive_values("deviceBatteryTags", self.device_battery_tags)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceManufacturerName", self.device_manufacturer_name)
        writer.write_str_value("deviceModelName", self.device_model_name)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_int_value("estimatedRuntimeInMinutes", self.estimated_runtime_in_minutes)
        writer.write_int_value("fullBatteryDrainCount", self.full_battery_drain_count)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_int_value("maxCapacityPercentage", self.max_capacity_percentage)
        writer.write_str_value("model", self.model)
    

