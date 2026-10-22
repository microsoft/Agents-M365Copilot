from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary

from .entity import Entity

@dataclass
class MacOSSoftwareUpdateAccountSummary(Entity, Parsable):
    """
    MacOS software update account summary report for a device and user
    """
    # Summary of the updates by category.
    category_summaries: Optional[list[MacOSSoftwareUpdateCategorySummary]] = None
    # The device ID.
    device_id: Optional[str] = None
    # The device name.
    device_name: Optional[str] = None
    # The name of the report
    display_name: Optional[str] = None
    # Number of failed updates on the device.
    failed_update_count: Optional[int] = None
    # Last date time the report for this device was updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The OS version.
    os_version: Optional[str] = None
    # Number of successful updates on the device.
    successful_update_count: Optional[int] = None
    # Number of total updates on the device.
    total_update_count: Optional[int] = None
    # The user ID.
    user_id: Optional[str] = None
    # The user principal name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSSoftwareUpdateAccountSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateAccountSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSSoftwareUpdateAccountSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary

        from .entity import Entity
        from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary

        fields: dict[str, Callable[[Any], None]] = {
            "categorySummaries": lambda n : setattr(self, 'category_summaries', n.get_collection_of_object_values(MacOSSoftwareUpdateCategorySummary)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "failedUpdateCount": lambda n : setattr(self, 'failed_update_count', n.get_int_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "successfulUpdateCount": lambda n : setattr(self, 'successful_update_count', n.get_int_value()),
            "totalUpdateCount": lambda n : setattr(self, 'total_update_count', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("categorySummaries", self.category_summaries)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("failedUpdateCount", self.failed_update_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_int_value("successfulUpdateCount", self.successful_update_count)
        writer.write_int_value("totalUpdateCount", self.total_update_count)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

