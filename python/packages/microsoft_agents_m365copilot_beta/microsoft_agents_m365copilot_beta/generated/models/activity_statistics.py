from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_activity_type import AnalyticsActivityType
    from .call_activity_statistics import CallActivityStatistics
    from .chat_activity_statistics import ChatActivityStatistics
    from .email_activity_statistics import EmailActivityStatistics
    from .entity import Entity
    from .focus_activity_statistics import FocusActivityStatistics
    from .meeting_activity_statistics import MeetingActivityStatistics

from .entity import Entity

@dataclass
class ActivityStatistics(Entity, Parsable):
    # The type of activity for which statistics are returned. The possible values are: call, chat, email, focus, and meeting.
    activity: Optional[AnalyticsActivityType] = None
    # Total hours spent on the activity. The value is represented in ISO 8601 format for durations.
    duration: Optional[datetime.timedelta] = None
    # Date when the activity ended, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-03' that follows the YYYY-MM-DD format.
    end_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date when the activity started, expressed in ISO 8601 format for calendar dates. For example, the property value could be '2019-07-04' that follows the YYYY-MM-DD format.
    start_date: Optional[datetime.date] = None
    # The time zone that the user sets in Microsoft Outlook is used for the computation. For example, the property value could be 'Pacific Standard Time.'
    time_zone_used: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivityStatistics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callActivityStatistics".casefold():
            from .call_activity_statistics import CallActivityStatistics

            return CallActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatActivityStatistics".casefold():
            from .chat_activity_statistics import ChatActivityStatistics

            return ChatActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailActivityStatistics".casefold():
            from .email_activity_statistics import EmailActivityStatistics

            return EmailActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.focusActivityStatistics".casefold():
            from .focus_activity_statistics import FocusActivityStatistics

            return FocusActivityStatistics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingActivityStatistics".casefold():
            from .meeting_activity_statistics import MeetingActivityStatistics

            return MeetingActivityStatistics()
        return ActivityStatistics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_activity_type import AnalyticsActivityType
        from .call_activity_statistics import CallActivityStatistics
        from .chat_activity_statistics import ChatActivityStatistics
        from .email_activity_statistics import EmailActivityStatistics
        from .entity import Entity
        from .focus_activity_statistics import FocusActivityStatistics
        from .meeting_activity_statistics import MeetingActivityStatistics

        from .analytics_activity_type import AnalyticsActivityType
        from .call_activity_statistics import CallActivityStatistics
        from .chat_activity_statistics import ChatActivityStatistics
        from .email_activity_statistics import EmailActivityStatistics
        from .entity import Entity
        from .focus_activity_statistics import FocusActivityStatistics
        from .meeting_activity_statistics import MeetingActivityStatistics

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(AnalyticsActivityType)),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "timeZoneUsed": lambda n : setattr(self, 'time_zone_used', n.get_str_value()),
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
        writer.write_enum_value("activity", self.activity)
        writer.write_timedelta_value("duration", self.duration)
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("startDate", self.start_date)
        writer.write_str_value("timeZoneUsed", self.time_zone_used)
    

