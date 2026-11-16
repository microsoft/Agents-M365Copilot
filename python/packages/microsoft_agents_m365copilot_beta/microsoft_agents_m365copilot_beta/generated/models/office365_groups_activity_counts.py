from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class Office365GroupsActivityCounts(Entity, Parsable):
    # The number of emails received by Group mailboxes.
    exchange_emails_received: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date on which a number of emails were sent to a group mailbox or a number of messages were posted, read, or liked in a Yammer group
    report_date: Optional[datetime.date] = None
    # The number of days the report covers.
    report_period: Optional[str] = None
    # The latest date of the content.
    report_refresh_date: Optional[datetime.date] = None
    # The number of channel messages in Teams team.
    teams_channel_messages: Optional[int] = None
    # The number of meetings organized in Teams team.
    teams_meetings_organized: Optional[int] = None
    # The number of messages liked in Yammer groups.
    yammer_messages_liked: Optional[int] = None
    # The number of messages posted to Yammer groups.
    yammer_messages_posted: Optional[int] = None
    # The number of messages read in Yammer groups.
    yammer_messages_read: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Office365GroupsActivityCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Office365GroupsActivityCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "exchangeEmailsReceived": lambda n : setattr(self, 'exchange_emails_received', n.get_int_value()),
            "reportDate": lambda n : setattr(self, 'report_date', n.get_date_value()),
            "reportPeriod": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "teamsChannelMessages": lambda n : setattr(self, 'teams_channel_messages', n.get_int_value()),
            "teamsMeetingsOrganized": lambda n : setattr(self, 'teams_meetings_organized', n.get_int_value()),
            "yammerMessagesLiked": lambda n : setattr(self, 'yammer_messages_liked', n.get_int_value()),
            "yammerMessagesPosted": lambda n : setattr(self, 'yammer_messages_posted', n.get_int_value()),
            "yammerMessagesRead": lambda n : setattr(self, 'yammer_messages_read', n.get_int_value()),
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
        writer.write_int_value("exchangeEmailsReceived", self.exchange_emails_received)
        writer.write_date_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("teamsChannelMessages", self.teams_channel_messages)
        writer.write_int_value("teamsMeetingsOrganized", self.teams_meetings_organized)
        writer.write_int_value("yammerMessagesLiked", self.yammer_messages_liked)
        writer.write_int_value("yammerMessagesPosted", self.yammer_messages_posted)
        writer.write_int_value("yammerMessagesRead", self.yammer_messages_read)
    

