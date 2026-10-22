from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_device_status import UserExperienceAnalyticsDeviceStatus

from .entity import Entity

@dataclass
class UserExperienceAnalyticsAnomalyDevice(Entity, Parsable):
    """
    The user experience analytics anomaly entity contains device details.
    """
    # The unique identifier of the anomaly.
    anomaly_id: Optional[str] = None
    # Indicates the first occurance date and time for the anomaly on the device.
    anomaly_on_device_first_occurrence_date_time: Optional[datetime.datetime] = None
    # Indicates the latest occurance date and time for the anomaly on the device.
    anomaly_on_device_latest_occurrence_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the correlation group.
    correlation_group_id: Optional[str] = None
    # The unique identifier of the device.
    device_id: Optional[str] = None
    # The manufacturer name of the device.
    device_manufacturer: Optional[str] = None
    # The model name of the device.
    device_model: Optional[str] = None
    # The name of the device.
    device_name: Optional[str] = None
    # Indicates the status of the device in the correlation group. Eg: Device status can be anomalous, affected, at risk.
    device_status: Optional[UserExperienceAnalyticsDeviceStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the OS installed on the device.
    os_name: Optional[str] = None
    # The OS version installed on the device.
    os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAnomalyDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalyDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAnomalyDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_device_status import UserExperienceAnalyticsDeviceStatus

        from .entity import Entity
        from .user_experience_analytics_device_status import UserExperienceAnalyticsDeviceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "anomalyId": lambda n : setattr(self, 'anomaly_id', n.get_str_value()),
            "anomalyOnDeviceFirstOccurrenceDateTime": lambda n : setattr(self, 'anomaly_on_device_first_occurrence_date_time', n.get_datetime_value()),
            "anomalyOnDeviceLatestOccurrenceDateTime": lambda n : setattr(self, 'anomaly_on_device_latest_occurrence_date_time', n.get_datetime_value()),
            "correlationGroupId": lambda n : setattr(self, 'correlation_group_id', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceManufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceStatus": lambda n : setattr(self, 'device_status', n.get_enum_value(UserExperienceAnalyticsDeviceStatus)),
            "osName": lambda n : setattr(self, 'os_name', n.get_str_value()),
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
        writer.write_str_value("anomalyId", self.anomaly_id)
        writer.write_datetime_value("anomalyOnDeviceFirstOccurrenceDateTime", self.anomaly_on_device_first_occurrence_date_time)
        writer.write_datetime_value("anomalyOnDeviceLatestOccurrenceDateTime", self.anomaly_on_device_latest_occurrence_date_time)
        writer.write_str_value("correlationGroupId", self.correlation_group_id)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceManufacturer", self.device_manufacturer)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("deviceStatus", self.device_status)
        writer.write_str_value("osName", self.os_name)
        writer.write_str_value("osVersion", self.os_version)
    

