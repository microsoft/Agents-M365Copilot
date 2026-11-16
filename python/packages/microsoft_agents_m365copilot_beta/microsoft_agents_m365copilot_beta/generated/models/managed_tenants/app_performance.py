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
class AppPerformance(Entity, Parsable):
    # The appFriendlyName property
    app_friendly_name: Optional[str] = None
    # The appName property
    app_name: Optional[str] = None
    # The appPublisher property
    app_publisher: Optional[str] = None
    # The lastUpdatedDateTime property
    last_updated_date_time: Optional[datetime.datetime] = None
    # The meanTimeToFailureInMinutes property
    mean_time_to_failure_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tenantDisplayName property
    tenant_display_name: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The totalActiveDeviceCount property
    total_active_device_count: Optional[int] = None
    # The totalAppCrashCount property
    total_app_crash_count: Optional[int] = None
    # The totalAppFreezeCount property
    total_app_freeze_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppPerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppPerformance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "appFriendlyName": lambda n : setattr(self, 'app_friendly_name', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appPublisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "meanTimeToFailureInMinutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "totalActiveDeviceCount": lambda n : setattr(self, 'total_active_device_count', n.get_int_value()),
            "totalAppCrashCount": lambda n : setattr(self, 'total_app_crash_count', n.get_int_value()),
            "totalAppFreezeCount": lambda n : setattr(self, 'total_app_freeze_count', n.get_int_value()),
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
        writer.write_str_value("appFriendlyName", self.app_friendly_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("totalActiveDeviceCount", self.total_active_device_count)
        writer.write_int_value("totalAppCrashCount", self.total_app_crash_count)
        writer.write_int_value("totalAppFreezeCount", self.total_app_freeze_count)
    

