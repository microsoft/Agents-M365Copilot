from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_event_level import DeviceEventLevel
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDeviceTimelineEvent(Entity, Parsable):
    """
    The user experience analytics device event entity contains NRT device event details.
    """
    # The id of the device where the event occurred.
    device_id: Optional[str] = None
    # The time the event occured.
    event_date_time: Optional[datetime.datetime] = None
    # The details provided by the event, format depends on event type.
    event_details: Optional[str] = None
    # Indicates device event level. Possible values are: None, Verbose, Information, Warning, Error, Critical
    event_level: Optional[DeviceEventLevel] = None
    # The name of the event. Examples include: BootEvent, LogonEvent, AppCrashEvent, AppHangEvent.
    event_name: Optional[str] = None
    # The source of the event. Examples include: Intune, Sccm.
    event_source: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsDeviceTimelineEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceTimelineEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceTimelineEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_event_level import DeviceEventLevel
        from .entity import Entity

        from .device_event_level import DeviceEventLevel
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventDetails": lambda n : setattr(self, 'event_details', n.get_str_value()),
            "eventLevel": lambda n : setattr(self, 'event_level', n.get_enum_value(DeviceEventLevel)),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "eventSource": lambda n : setattr(self, 'event_source', n.get_str_value()),
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
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventDetails", self.event_details)
        writer.write_enum_value("eventLevel", self.event_level)
        writer.write_str_value("eventName", self.event_name)
        writer.write_str_value("eventSource", self.event_source)
    

