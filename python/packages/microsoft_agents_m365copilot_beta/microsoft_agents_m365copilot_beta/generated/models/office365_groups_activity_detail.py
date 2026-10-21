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
class Office365GroupsActivityDetail(Entity, Parsable):
    # The storage used of the group mailbox.
    exchange_mailbox_storage_used_in_bytes: Optional[int] = None
    # The number of items in the group mailbox.
    exchange_mailbox_total_item_count: Optional[int] = None
    # The number of emails that the group mailbox received.
    exchange_received_email_count: Optional[int] = None
    # The group external member count.
    external_member_count: Optional[int] = None
    # The display name of the group.
    group_display_name: Optional[str] = None
    # The group id.
    group_id: Optional[str] = None
    # The group type. The possible values are: Public or Private.
    group_type: Optional[str] = None
    # Whether this user has been deleted or soft deleted.
    is_deleted: Optional[bool] = None
    # The last activity date for the following scenarios:  group mailbox received email; user viewed, edited, shared, or synced files in SharePoint document library; user viewed SharePoint pages; user posted, read, or liked messages in Yammer groups.
    last_activity_date: Optional[datetime.date] = None
    # The group member count.
    member_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The group owner principal name.
    owner_principal_name: Optional[str] = None
    # The number of days the report covers.
    report_period: Optional[str] = None
    # The latest date of the content.
    report_refresh_date: Optional[datetime.date] = None
    # The number of active files in SharePoint Group site.
    share_point_active_file_count: Optional[int] = None
    # The storage used by SharePoint Group site.
    share_point_site_storage_used_in_bytes: Optional[int] = None
    # The total number of files in SharePoint Group site.
    share_point_total_file_count: Optional[int] = None
    # The number of channel messages in Teams team.
    teams_channel_messages_count: Optional[int] = None
    # The number of meetings organized in Teams team.
    teams_meetings_organized_count: Optional[int] = None
    # The number of messages liked in Yammer groups.
    yammer_liked_message_count: Optional[int] = None
    # The number of messages posted to Yammer groups.
    yammer_posted_message_count: Optional[int] = None
    # The number of messages read in Yammer groups.
    yammer_read_message_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Office365GroupsActivityDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Office365GroupsActivityDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "exchangeMailboxStorageUsedInBytes": lambda n : setattr(self, 'exchange_mailbox_storage_used_in_bytes', n.get_int_value()),
            "exchangeMailboxTotalItemCount": lambda n : setattr(self, 'exchange_mailbox_total_item_count', n.get_int_value()),
            "exchangeReceivedEmailCount": lambda n : setattr(self, 'exchange_received_email_count', n.get_int_value()),
            "externalMemberCount": lambda n : setattr(self, 'external_member_count', n.get_int_value()),
            "groupDisplayName": lambda n : setattr(self, 'group_display_name', n.get_str_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "groupType": lambda n : setattr(self, 'group_type', n.get_str_value()),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "lastActivityDate": lambda n : setattr(self, 'last_activity_date', n.get_date_value()),
            "memberCount": lambda n : setattr(self, 'member_count', n.get_int_value()),
            "ownerPrincipalName": lambda n : setattr(self, 'owner_principal_name', n.get_str_value()),
            "reportPeriod": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "sharePointActiveFileCount": lambda n : setattr(self, 'share_point_active_file_count', n.get_int_value()),
            "sharePointSiteStorageUsedInBytes": lambda n : setattr(self, 'share_point_site_storage_used_in_bytes', n.get_int_value()),
            "sharePointTotalFileCount": lambda n : setattr(self, 'share_point_total_file_count', n.get_int_value()),
            "teamsChannelMessagesCount": lambda n : setattr(self, 'teams_channel_messages_count', n.get_int_value()),
            "teamsMeetingsOrganizedCount": lambda n : setattr(self, 'teams_meetings_organized_count', n.get_int_value()),
            "yammerLikedMessageCount": lambda n : setattr(self, 'yammer_liked_message_count', n.get_int_value()),
            "yammerPostedMessageCount": lambda n : setattr(self, 'yammer_posted_message_count', n.get_int_value()),
            "yammerReadMessageCount": lambda n : setattr(self, 'yammer_read_message_count', n.get_int_value()),
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
        writer.write_int_value("exchangeMailboxStorageUsedInBytes", self.exchange_mailbox_storage_used_in_bytes)
        writer.write_int_value("exchangeMailboxTotalItemCount", self.exchange_mailbox_total_item_count)
        writer.write_int_value("exchangeReceivedEmailCount", self.exchange_received_email_count)
        writer.write_int_value("externalMemberCount", self.external_member_count)
        writer.write_str_value("groupDisplayName", self.group_display_name)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("groupType", self.group_type)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_date_value("lastActivityDate", self.last_activity_date)
        writer.write_int_value("memberCount", self.member_count)
        writer.write_str_value("ownerPrincipalName", self.owner_principal_name)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("sharePointActiveFileCount", self.share_point_active_file_count)
        writer.write_int_value("sharePointSiteStorageUsedInBytes", self.share_point_site_storage_used_in_bytes)
        writer.write_int_value("sharePointTotalFileCount", self.share_point_total_file_count)
        writer.write_int_value("teamsChannelMessagesCount", self.teams_channel_messages_count)
        writer.write_int_value("teamsMeetingsOrganizedCount", self.teams_meetings_organized_count)
        writer.write_int_value("yammerLikedMessageCount", self.yammer_liked_message_count)
        writer.write_int_value("yammerPostedMessageCount", self.yammer_posted_message_count)
        writer.write_int_value("yammerReadMessageCount", self.yammer_read_message_count)
    

