from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBatteryHealthOsPerformance(Entity, Parsable):
    """
    The user experience analytics battery health os performance entity contains battery related information for all operating system versions in their organization.
    """
    # Number of active devices for that os version. Valid values 0 to 2147483647
    active_devices: Optional[int] = None
    # The mean of the battery age for all devices running a particular operating system version in a tenant. Unit in days. Valid values 0 to 2147483647
    average_battery_age_in_days: Optional[int] = None
    # The mean of the estimated runtimes on full charge for all devices running a particular operating system version. Unit in minutes. Valid values 0 to 2147483647
    average_estimated_runtime_in_minutes: Optional[int] = None
    # The mean of the maximum capacity for all devices running a particular operating system version. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values 0 to 2147483647
    average_max_capacity_percentage: Optional[int] = None
    # The mean of number of times the battery has been discharged an amount that equals 100% of its capacity for all devices running a particular operating system version in a tenant. Valid values 0 to 2147483647
    mean_full_battery_drain_count: Optional[int] = None
    # The median of the estimated runtimes on full charge for all devices running a particular operating system version. Unit in minutes. Valid values 0 to 2147483647
    median_estimated_runtime_in_minutes: Optional[int] = None
    # The median of number of times the battery has been discharged an amount that equals 100% of its capacity for all devices running a particular operating system version in a tenant. Valid values 0 to 2147483647
    median_full_battery_drain_count: Optional[int] = None
    # The median of the maximum capacity for all devices running a particular operating system version. Maximum capacity measures the full charge vs. design capacity for a device’s batteries.. Valid values 0 to 2147483647
    median_max_capacity_percentage: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A weighted average of battery health score across all devices running a particular operating system version. Values range from 0-100. Valid values 0 to 2147483647
    os_battery_health_score: Optional[int] = None
    # Build number of the operating system.
    os_build_number: Optional[str] = None
    # The osHealthStatus property
    os_health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # Version of the operating system.
    os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsBatteryHealthOsPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthOsPerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthOsPerformance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        fields: dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "averageBatteryAgeInDays": lambda n : setattr(self, 'average_battery_age_in_days', n.get_int_value()),
            "averageEstimatedRuntimeInMinutes": lambda n : setattr(self, 'average_estimated_runtime_in_minutes', n.get_int_value()),
            "averageMaxCapacityPercentage": lambda n : setattr(self, 'average_max_capacity_percentage', n.get_int_value()),
            "meanFullBatteryDrainCount": lambda n : setattr(self, 'mean_full_battery_drain_count', n.get_int_value()),
            "medianEstimatedRuntimeInMinutes": lambda n : setattr(self, 'median_estimated_runtime_in_minutes', n.get_int_value()),
            "medianFullBatteryDrainCount": lambda n : setattr(self, 'median_full_battery_drain_count', n.get_int_value()),
            "medianMaxCapacityPercentage": lambda n : setattr(self, 'median_max_capacity_percentage', n.get_int_value()),
            "osBatteryHealthScore": lambda n : setattr(self, 'os_battery_health_score', n.get_int_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "osHealthStatus": lambda n : setattr(self, 'os_health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
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
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_int_value("averageBatteryAgeInDays", self.average_battery_age_in_days)
        writer.write_int_value("averageEstimatedRuntimeInMinutes", self.average_estimated_runtime_in_minutes)
        writer.write_int_value("averageMaxCapacityPercentage", self.average_max_capacity_percentage)
        writer.write_int_value("meanFullBatteryDrainCount", self.mean_full_battery_drain_count)
        writer.write_int_value("medianEstimatedRuntimeInMinutes", self.median_estimated_runtime_in_minutes)
        writer.write_int_value("medianFullBatteryDrainCount", self.median_full_battery_drain_count)
        writer.write_int_value("medianMaxCapacityPercentage", self.median_max_capacity_percentage)
        writer.write_int_value("osBatteryHealthScore", self.os_battery_health_score)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_enum_value("osHealthStatus", self.os_health_status)
        writer.write_str_value("osVersion", self.os_version)
    

