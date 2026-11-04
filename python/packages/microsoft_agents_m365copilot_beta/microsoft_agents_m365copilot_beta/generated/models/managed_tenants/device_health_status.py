from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class DeviceHealthStatus(Entity, Parsable):
    # The blueScreenCount property
    blue_screen_count: Optional[int] = None
    # The bootTotalDurationInSeconds property
    boot_total_duration_in_seconds: Optional[float] = None
    # The deviceId property
    device_id: Optional[str] = None
    # The deviceMake property
    device_make: Optional[str] = None
    # The deviceModel property
    device_model: Optional[str] = None
    # The deviceName property
    device_name: Optional[str] = None
    # The healthStatus property
    health_status: Optional[str] = None
    # The lastUpdatedDateTime property
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The osVersion property
    os_version: Optional[str] = None
    # The primaryDiskType property
    primary_disk_type: Optional[str] = None
    # The restartCount property
    restart_count: Optional[int] = None
    # The startupPerformanceScore property
    startup_performance_score: Optional[float] = None
    # The tenantDisplayName property
    tenant_display_name: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The topProcesses property
    top_processes: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "blueScreenCount": lambda n : setattr(self, 'blue_screen_count', n.get_int_value()),
            "bootTotalDurationInSeconds": lambda n : setattr(self, 'boot_total_duration_in_seconds', n.get_float_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceMake": lambda n : setattr(self, 'device_make', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "primaryDiskType": lambda n : setattr(self, 'primary_disk_type', n.get_str_value()),
            "restartCount": lambda n : setattr(self, 'restart_count', n.get_int_value()),
            "startupPerformanceScore": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "topProcesses": lambda n : setattr(self, 'top_processes', n.get_str_value()),
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
        writer.write_int_value("blueScreenCount", self.blue_screen_count)
        writer.write_float_value("bootTotalDurationInSeconds", self.boot_total_duration_in_seconds)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceMake", self.device_make)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("healthStatus", self.health_status)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("primaryDiskType", self.primary_disk_type)
        writer.write_int_value("restartCount", self.restart_count)
        writer.write_float_value("startupPerformanceScore", self.startup_performance_score)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("topProcesses", self.top_processes)
    

