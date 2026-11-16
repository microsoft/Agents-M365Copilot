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
class Office365ActiveUserCounts(Entity, Parsable):
    # The number of active users in Exchange. Any user who can read and send email is considered an active user.
    exchange: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of active users in Microsoft 365. This number includes all the active users in Exchange, OneDrive, SharePoint, Skype For Business, Yammer, and Microsoft Teams. You can find the definition of active user for each product in the respective property description.
    office365: Optional[int] = None
    # The number of active users in OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
    one_drive: Optional[int] = None
    # The date on which a number of users were active.
    report_date: Optional[datetime.date] = None
    # The number of days the report covers.
    report_period: Optional[str] = None
    # The latest date of the content.
    report_refresh_date: Optional[datetime.date] = None
    # The number of active users in SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
    share_point: Optional[int] = None
    # The number of active users in Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
    skype_for_business: Optional[int] = None
    # The number of active users in Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
    teams: Optional[int] = None
    # The number of active users in Yammer. Any user who can post, read, or like messages is considered an active user.
    yammer: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Office365ActiveUserCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Office365ActiveUserCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Office365ActiveUserCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "exchange": lambda n : setattr(self, 'exchange', n.get_int_value()),
            "office365": lambda n : setattr(self, 'office365', n.get_int_value()),
            "oneDrive": lambda n : setattr(self, 'one_drive', n.get_int_value()),
            "reportDate": lambda n : setattr(self, 'report_date', n.get_date_value()),
            "reportPeriod": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "sharePoint": lambda n : setattr(self, 'share_point', n.get_int_value()),
            "skypeForBusiness": lambda n : setattr(self, 'skype_for_business', n.get_int_value()),
            "teams": lambda n : setattr(self, 'teams', n.get_int_value()),
            "yammer": lambda n : setattr(self, 'yammer', n.get_int_value()),
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
        writer.write_int_value("exchange", self.exchange)
        writer.write_int_value("office365", self.office365)
        writer.write_int_value("oneDrive", self.one_drive)
        writer.write_date_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("sharePoint", self.share_point)
        writer.write_int_value("skypeForBusiness", self.skype_for_business)
        writer.write_int_value("teams", self.teams)
        writer.write_int_value("yammer", self.yammer)
    

