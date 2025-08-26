from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_info import ChatInfo
    from .entity import Entity
    from .meeting_info import MeetingInfo
    from .subscription_activities import SubscriptionActivities

from .entity import Entity

@dataclass
class MultiActivitySubscription(Entity, Parsable):
    # The activities property
    activities: Optional[SubscriptionActivities] = None
    # The callbackUrl property
    callback_url: Optional[str] = None
    # The chatInfo property
    chat_info: Optional[ChatInfo] = None
    # The meetingInfo property
    meeting_info: Optional[MeetingInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiActivitySubscription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiActivitySubscription
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiActivitySubscription()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_info import ChatInfo
        from .entity import Entity
        from .meeting_info import MeetingInfo
        from .subscription_activities import SubscriptionActivities

        from .chat_info import ChatInfo
        from .entity import Entity
        from .meeting_info import MeetingInfo
        from .subscription_activities import SubscriptionActivities

        fields: dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_object_value(SubscriptionActivities)),
            "callbackUrl": lambda n : setattr(self, 'callback_url', n.get_str_value()),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "meetingInfo": lambda n : setattr(self, 'meeting_info', n.get_object_value(MeetingInfo)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("activities", self.activities)
        writer.write_str_value("callbackUrl", self.callback_url)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_object_value("meetingInfo", self.meeting_info)
        writer.write_str_value("userId", self.user_id)
    

