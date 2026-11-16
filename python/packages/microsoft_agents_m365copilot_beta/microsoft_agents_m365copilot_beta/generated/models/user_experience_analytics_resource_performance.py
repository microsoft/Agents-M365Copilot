from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disk_type import DiskType
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
    from .user_experience_analytics_machine_type import UserExperienceAnalyticsMachineType

from .entity import Entity

@dataclass
class UserExperienceAnalyticsResourcePerformance(Entity, Parsable):
    """
    The user experience analytics resource performance entity.
    """
    # AverageSpikeTimeScore of a device or a model type. Valid values 0 to 100
    average_spike_time_score: Optional[int] = None
    # The clock speed of the processor, in MHz. Valid values 0 to 1000000
    cpu_clock_speed_in_m_hz: Optional[float] = None
    # The name of the processor on the device, For example, 11th Gen Intel(R) Core(TM) i7.
    cpu_display_name: Optional[str] = None
    # CPU spike time in percentage. Valid values 0 to 100
    cpu_spike_time_percentage: Optional[float] = None
    # Threshold of cpuSpikeTimeScore. Valid values 0 to 100
    cpu_spike_time_percentage_threshold: Optional[float] = None
    # The user experience analytics device CPU spike time score. Valid values 0 to 100
    cpu_spike_time_score: Optional[int] = None
    # User experience analytics summarized device count.
    device_count: Optional[int] = None
    # The id of the device.
    device_id: Optional[str] = None
    # The name of the device.
    device_name: Optional[str] = None
    # Resource performance score of a specific device. Valid values 0 to 100
    device_resource_performance_score: Optional[int] = None
    # The diskType property
    disk_type: Optional[DiskType] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # Indicates if machine is physical or virtual. Possible values are: physical or virtual
    machine_type: Optional[UserExperienceAnalyticsMachineType] = None
    # The user experience analytics device manufacturer.
    manufacturer: Optional[str] = None
    # The user experience analytics device model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # RAM spike time in percentage. Valid values 0 to 100
    ram_spike_time_percentage: Optional[float] = None
    # Threshold of ramSpikeTimeScore. Valid values 0 to 100
    ram_spike_time_percentage_threshold: Optional[float] = None
    # The user experience analytics device RAM spike time score. Valid values 0 to 100
    ram_spike_time_score: Optional[int] = None
    # The count of cores of the processor of device. Valid values 0 to 512
    total_processor_core_count: Optional[int] = None
    # The total RAM of the device, in MB. Valid values 0 to 1000000
    total_ram_in_m_b: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsResourcePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsResourcePerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsResourcePerformance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .disk_type import DiskType
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
        from .user_experience_analytics_machine_type import UserExperienceAnalyticsMachineType

        from .disk_type import DiskType
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
        from .user_experience_analytics_machine_type import UserExperienceAnalyticsMachineType

        fields: dict[str, Callable[[Any], None]] = {
            "averageSpikeTimeScore": lambda n : setattr(self, 'average_spike_time_score', n.get_int_value()),
            "cpuClockSpeedInMHz": lambda n : setattr(self, 'cpu_clock_speed_in_m_hz', n.get_float_value()),
            "cpuDisplayName": lambda n : setattr(self, 'cpu_display_name', n.get_str_value()),
            "cpuSpikeTimePercentage": lambda n : setattr(self, 'cpu_spike_time_percentage', n.get_float_value()),
            "cpuSpikeTimePercentageThreshold": lambda n : setattr(self, 'cpu_spike_time_percentage_threshold', n.get_float_value()),
            "cpuSpikeTimeScore": lambda n : setattr(self, 'cpu_spike_time_score', n.get_int_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceResourcePerformanceScore": lambda n : setattr(self, 'device_resource_performance_score', n.get_int_value()),
            "diskType": lambda n : setattr(self, 'disk_type', n.get_enum_value(DiskType)),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "machineType": lambda n : setattr(self, 'machine_type', n.get_enum_value(UserExperienceAnalyticsMachineType)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "ramSpikeTimePercentage": lambda n : setattr(self, 'ram_spike_time_percentage', n.get_float_value()),
            "ramSpikeTimePercentageThreshold": lambda n : setattr(self, 'ram_spike_time_percentage_threshold', n.get_float_value()),
            "ramSpikeTimeScore": lambda n : setattr(self, 'ram_spike_time_score', n.get_int_value()),
            "totalProcessorCoreCount": lambda n : setattr(self, 'total_processor_core_count', n.get_int_value()),
            "totalRamInMB": lambda n : setattr(self, 'total_ram_in_m_b', n.get_float_value()),
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
        writer.write_int_value("averageSpikeTimeScore", self.average_spike_time_score)
        writer.write_float_value("cpuClockSpeedInMHz", self.cpu_clock_speed_in_m_hz)
        writer.write_str_value("cpuDisplayName", self.cpu_display_name)
        writer.write_float_value("cpuSpikeTimePercentage", self.cpu_spike_time_percentage)
        writer.write_float_value("cpuSpikeTimePercentageThreshold", self.cpu_spike_time_percentage_threshold)
        writer.write_int_value("cpuSpikeTimeScore", self.cpu_spike_time_score)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_int_value("deviceResourcePerformanceScore", self.device_resource_performance_score)
        writer.write_enum_value("diskType", self.disk_type)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_enum_value("machineType", self.machine_type)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("ramSpikeTimePercentage", self.ram_spike_time_percentage)
        writer.write_float_value("ramSpikeTimePercentageThreshold", self.ram_spike_time_percentage_threshold)
        writer.write_int_value("ramSpikeTimeScore", self.ram_spike_time_score)
        writer.write_int_value("totalProcessorCoreCount", self.total_processor_core_count)
        writer.write_float_value("totalRamInMB", self.total_ram_in_m_b)
    

