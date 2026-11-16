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
class Office365ActiveUserDetail(Entity, Parsable):
    # All the products assigned for the user.
    assigned_products: Optional[list[str]] = None
    # The date when the delete operation happened. Default value is 'null' when the user hasn't been deleted.
    deleted_date: Optional[datetime.date] = None
    # The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it can't be cleared during updates.
    display_name: Optional[str] = None
    # The date when user last read or sent email.
    exchange_last_activity_date: Optional[datetime.date] = None
    # The last date when the user was assigned an Exchange license.
    exchange_license_assign_date: Optional[datetime.date] = None
    # Whether the user has been assigned an Exchange license.
    has_exchange_license: Optional[bool] = None
    # Whether the user has been assigned a OneDrive license.
    has_one_drive_license: Optional[bool] = None
    # Whether the user has been assigned a SharePoint license.
    has_share_point_license: Optional[bool] = None
    # Whether the user has been assigned a Skype For Business license.
    has_skype_for_business_license: Optional[bool] = None
    # Whether the user has been assigned a Teams license.
    has_teams_license: Optional[bool] = None
    # Whether the user has been assigned a Yammer license.
    has_yammer_license: Optional[bool] = None
    # Whether this user has been deleted or soft deleted.
    is_deleted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date when user last viewed or edited files, shared files internally or externally, or synced files.
    one_drive_last_activity_date: Optional[datetime.date] = None
    # The last date when the user was assigned a OneDrive license.
    one_drive_license_assign_date: Optional[datetime.date] = None
    # The latest date of the content.
    report_refresh_date: Optional[datetime.date] = None
    # The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
    share_point_last_activity_date: Optional[datetime.date] = None
    # The last date when the user was assigned a SharePoint license.
    share_point_license_assign_date: Optional[datetime.date] = None
    # The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
    skype_for_business_last_activity_date: Optional[datetime.date] = None
    # The last date when the user was assigned a Skype For Business license.
    skype_for_business_license_assign_date: Optional[datetime.date] = None
    # The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
    teams_last_activity_date: Optional[datetime.date] = None
    # The last date when the user was assigned a Teams license.
    teams_license_assign_date: Optional[datetime.date] = None
    # The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. This property is required when a user is created.
    user_principal_name: Optional[str] = None
    # The date when user last posted, read, or liked message.
    yammer_last_activity_date: Optional[datetime.date] = None
    # The last date when the user was assigned a Yammer license.
    yammer_license_assign_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Office365ActiveUserDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Office365ActiveUserDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Office365ActiveUserDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignedProducts": lambda n : setattr(self, 'assigned_products', n.get_collection_of_primitive_values(str)),
            "deletedDate": lambda n : setattr(self, 'deleted_date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exchangeLastActivityDate": lambda n : setattr(self, 'exchange_last_activity_date', n.get_date_value()),
            "exchangeLicenseAssignDate": lambda n : setattr(self, 'exchange_license_assign_date', n.get_date_value()),
            "hasExchangeLicense": lambda n : setattr(self, 'has_exchange_license', n.get_bool_value()),
            "hasOneDriveLicense": lambda n : setattr(self, 'has_one_drive_license', n.get_bool_value()),
            "hasSharePointLicense": lambda n : setattr(self, 'has_share_point_license', n.get_bool_value()),
            "hasSkypeForBusinessLicense": lambda n : setattr(self, 'has_skype_for_business_license', n.get_bool_value()),
            "hasTeamsLicense": lambda n : setattr(self, 'has_teams_license', n.get_bool_value()),
            "hasYammerLicense": lambda n : setattr(self, 'has_yammer_license', n.get_bool_value()),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "oneDriveLastActivityDate": lambda n : setattr(self, 'one_drive_last_activity_date', n.get_date_value()),
            "oneDriveLicenseAssignDate": lambda n : setattr(self, 'one_drive_license_assign_date', n.get_date_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "sharePointLastActivityDate": lambda n : setattr(self, 'share_point_last_activity_date', n.get_date_value()),
            "sharePointLicenseAssignDate": lambda n : setattr(self, 'share_point_license_assign_date', n.get_date_value()),
            "skypeForBusinessLastActivityDate": lambda n : setattr(self, 'skype_for_business_last_activity_date', n.get_date_value()),
            "skypeForBusinessLicenseAssignDate": lambda n : setattr(self, 'skype_for_business_license_assign_date', n.get_date_value()),
            "teamsLastActivityDate": lambda n : setattr(self, 'teams_last_activity_date', n.get_date_value()),
            "teamsLicenseAssignDate": lambda n : setattr(self, 'teams_license_assign_date', n.get_date_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "yammerLastActivityDate": lambda n : setattr(self, 'yammer_last_activity_date', n.get_date_value()),
            "yammerLicenseAssignDate": lambda n : setattr(self, 'yammer_license_assign_date', n.get_date_value()),
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
        writer.write_collection_of_primitive_values("assignedProducts", self.assigned_products)
        writer.write_date_value("deletedDate", self.deleted_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("exchangeLastActivityDate", self.exchange_last_activity_date)
        writer.write_date_value("exchangeLicenseAssignDate", self.exchange_license_assign_date)
        writer.write_bool_value("hasExchangeLicense", self.has_exchange_license)
        writer.write_bool_value("hasOneDriveLicense", self.has_one_drive_license)
        writer.write_bool_value("hasSharePointLicense", self.has_share_point_license)
        writer.write_bool_value("hasSkypeForBusinessLicense", self.has_skype_for_business_license)
        writer.write_bool_value("hasTeamsLicense", self.has_teams_license)
        writer.write_bool_value("hasYammerLicense", self.has_yammer_license)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_date_value("oneDriveLastActivityDate", self.one_drive_last_activity_date)
        writer.write_date_value("oneDriveLicenseAssignDate", self.one_drive_license_assign_date)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_date_value("sharePointLastActivityDate", self.share_point_last_activity_date)
        writer.write_date_value("sharePointLicenseAssignDate", self.share_point_license_assign_date)
        writer.write_date_value("skypeForBusinessLastActivityDate", self.skype_for_business_last_activity_date)
        writer.write_date_value("skypeForBusinessLicenseAssignDate", self.skype_for_business_license_assign_date)
        writer.write_date_value("teamsLastActivityDate", self.teams_last_activity_date)
        writer.write_date_value("teamsLicenseAssignDate", self.teams_license_assign_date)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_date_value("yammerLastActivityDate", self.yammer_last_activity_date)
        writer.write_date_value("yammerLicenseAssignDate", self.yammer_license_assign_date)
    

