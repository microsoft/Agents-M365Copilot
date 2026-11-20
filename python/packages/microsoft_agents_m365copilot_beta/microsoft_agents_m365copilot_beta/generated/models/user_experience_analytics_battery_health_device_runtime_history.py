from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory(Entity, Parsable):
    """
    The user experience analytics battery health runtime history entity contains the trend of runtime of a device over a period of 30 days
    """
    # The unique identifier of the device, Intune DeviceID or SCCM device id.
    device_id: Optional[str] = None
    # The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values 0 to 2147483647
    estimated_runtime_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The datetime for the instance of runtime history.
    runtime_date_time: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "estimatedRuntimeInMinutes": lambda n : setattr(self, 'estimated_runtime_in_minutes', n.get_int_value()),
            "runtimeDateTime": lambda n : setattr(self, 'runtime_date_time', n.get_str_value()),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_int_value("estimatedRuntimeInMinutes", self.estimated_runtime_in_minutes)
        writer.write_str_value("runtimeDateTime", self.runtime_date_time)
    

