from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .payload_types import PayloadTypes
    from .priority import Priority
    from .target_policy_endpoints import TargetPolicyEndpoints

from .entity import Entity

@dataclass
class Notification(Entity, Parsable):
    # Sets how long (in seconds) this notification content stays in each platform's notification viewer. For example, when the notification is delivered to a Windows device, the value of this property is passed on to ToastNotification.ExpirationTime, which determines how long the toast notification stays in the user's Windows Action Center.
    display_time_to_live: Optional[int] = None
    # Sets a UTC expiration date and time on a user notification using ISO 8601 format (for example, midnight UTC on Jan 1, 2019 would look like this: '2019-01-01T00:00:00Z'). When time is up, the notification is removed from the Microsoft Graph notification feed store completely and is no longer part of notification history. Max value is 30 days.
    expiration_date_time: Optional[datetime.datetime] = None
    # The name of the group that this notification belongs to. It is set by the developer for grouping notifications together.
    group_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The payload property
    payload: Optional[PayloadTypes] = None
    # Indicates the priority of a raw user notification. Visual notifications are sent with high priority by default. Valid values are None, High and Low.
    priority: Optional[Priority] = None
    # Represents the host name of the app to which the calling service wants to post the notification, for the given user. If targeting web endpoints (see targetPolicy.platformTypes), ensure that targetHostName is the same as the name used when creating a subscription on the client side within the application JSON property.
    target_host_name: Optional[str] = None
    # Target policy object handles notification delivery policy for endpoint types that should be targeted (Windows, iOS, Android and WebPush) for the given user.
    target_policy: Optional[TargetPolicyEndpoints] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Notification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Notification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Notification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .payload_types import PayloadTypes
        from .priority import Priority
        from .target_policy_endpoints import TargetPolicyEndpoints

        from .entity import Entity
        from .payload_types import PayloadTypes
        from .priority import Priority
        from .target_policy_endpoints import TargetPolicyEndpoints

        fields: dict[str, Callable[[Any], None]] = {
            "displayTimeToLive": lambda n : setattr(self, 'display_time_to_live', n.get_int_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_object_value(PayloadTypes)),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(Priority)),
            "targetHostName": lambda n : setattr(self, 'target_host_name', n.get_str_value()),
            "targetPolicy": lambda n : setattr(self, 'target_policy', n.get_object_value(TargetPolicyEndpoints)),
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
        writer.write_int_value("displayTimeToLive", self.display_time_to_live)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("groupName", self.group_name)
        writer.write_object_value("payload", self.payload)
        writer.write_enum_value("priority", self.priority)
        writer.write_str_value("targetHostName", self.target_host_name)
        writer.write_object_value("targetPolicy", self.target_policy)
    

