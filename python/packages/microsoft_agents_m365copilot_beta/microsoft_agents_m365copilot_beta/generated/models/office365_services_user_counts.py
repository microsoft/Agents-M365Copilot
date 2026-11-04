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
class Office365ServicesUserCounts(Entity, Parsable):
    # The number of active users on Exchange. Any user who can read and send email is considered an active user.
    exchange_active: Optional[int] = None
    # The number of inactive users on Exchange.
    exchange_inactive: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of active users on Microsoft 365.
    office365_active: Optional[int] = None
    # The number of inactive users on Microsoft 365.
    office365_inactive: Optional[int] = None
    # The number of active users on OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
    one_drive_active: Optional[int] = None
    # The number of inactive users on OneDrive.
    one_drive_inactive: Optional[int] = None
    # The number of days the report covers.
    report_period: Optional[str] = None
    # The latest date of the content.
    report_refresh_date: Optional[datetime.date] = None
    # The number of active users on SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
    share_point_active: Optional[int] = None
    # The number of inactive users on SharePoint.
    share_point_inactive: Optional[int] = None
    # The number of active users on Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
    skype_for_business_active: Optional[int] = None
    # The number of inactive users on Skype For Business.
    skype_for_business_inactive: Optional[int] = None
    # The number of active users on Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
    teams_active: Optional[int] = None
    # The number of inactive users on Microsoft Teams.
    teams_inactive: Optional[int] = None
    # The number of active users on Yammer. Any user who can post, read, or like messages is considered an active user.
    yammer_active: Optional[int] = None
    # The number of inactive users on Yammer.
    yammer_inactive: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Office365ServicesUserCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Office365ServicesUserCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Office365ServicesUserCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "exchangeActive": lambda n : setattr(self, 'exchange_active', n.get_int_value()),
            "exchangeInactive": lambda n : setattr(self, 'exchange_inactive', n.get_int_value()),
            "office365Active": lambda n : setattr(self, 'office365_active', n.get_int_value()),
            "office365Inactive": lambda n : setattr(self, 'office365_inactive', n.get_int_value()),
            "oneDriveActive": lambda n : setattr(self, 'one_drive_active', n.get_int_value()),
            "oneDriveInactive": lambda n : setattr(self, 'one_drive_inactive', n.get_int_value()),
            "reportPeriod": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "sharePointActive": lambda n : setattr(self, 'share_point_active', n.get_int_value()),
            "sharePointInactive": lambda n : setattr(self, 'share_point_inactive', n.get_int_value()),
            "skypeForBusinessActive": lambda n : setattr(self, 'skype_for_business_active', n.get_int_value()),
            "skypeForBusinessInactive": lambda n : setattr(self, 'skype_for_business_inactive', n.get_int_value()),
            "teamsActive": lambda n : setattr(self, 'teams_active', n.get_int_value()),
            "teamsInactive": lambda n : setattr(self, 'teams_inactive', n.get_int_value()),
            "yammerActive": lambda n : setattr(self, 'yammer_active', n.get_int_value()),
            "yammerInactive": lambda n : setattr(self, 'yammer_inactive', n.get_int_value()),
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
        writer.write_int_value("exchangeActive", self.exchange_active)
        writer.write_int_value("exchangeInactive", self.exchange_inactive)
        writer.write_int_value("office365Active", self.office365_active)
        writer.write_int_value("office365Inactive", self.office365_inactive)
        writer.write_int_value("oneDriveActive", self.one_drive_active)
        writer.write_int_value("oneDriveInactive", self.one_drive_inactive)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("sharePointActive", self.share_point_active)
        writer.write_int_value("sharePointInactive", self.share_point_inactive)
        writer.write_int_value("skypeForBusinessActive", self.skype_for_business_active)
        writer.write_int_value("skypeForBusinessInactive", self.skype_for_business_inactive)
        writer.write_int_value("teamsActive", self.teams_active)
        writer.write_int_value("teamsInactive", self.teams_inactive)
        writer.write_int_value("yammerActive", self.yammer_active)
        writer.write_int_value("yammerInactive", self.yammer_inactive)
    

