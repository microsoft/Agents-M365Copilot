from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
    from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary

from .entity import Entity

@dataclass
class MacOSSoftwareUpdateCategorySummary(Entity, Parsable):
    """
    MacOS software update category summary report for a device and user
    """
    # The device ID.
    device_id: Optional[str] = None
    # The name of the report
    display_name: Optional[str] = None
    # Number of failed updates on the device
    failed_update_count: Optional[int] = None
    # Last date time the report for this device was updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of successful updates on the device
    successful_update_count: Optional[int] = None
    # Number of total updates on the device
    total_update_count: Optional[int] = None
    # MacOS Software Update Category
    update_category: Optional[MacOSSoftwareUpdateCategory] = None
    # Summary of the update states.
    update_state_summaries: Optional[list[MacOSSoftwareUpdateStateSummary]] = None
    # The user ID.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSSoftwareUpdateCategorySummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateCategorySummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSSoftwareUpdateCategorySummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
        from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary

        from .entity import Entity
        from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
        from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "failedUpdateCount": lambda n : setattr(self, 'failed_update_count', n.get_int_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "successfulUpdateCount": lambda n : setattr(self, 'successful_update_count', n.get_int_value()),
            "totalUpdateCount": lambda n : setattr(self, 'total_update_count', n.get_int_value()),
            "updateCategory": lambda n : setattr(self, 'update_category', n.get_enum_value(MacOSSoftwareUpdateCategory)),
            "updateStateSummaries": lambda n : setattr(self, 'update_state_summaries', n.get_collection_of_object_values(MacOSSoftwareUpdateStateSummary)),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("failedUpdateCount", self.failed_update_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("successfulUpdateCount", self.successful_update_count)
        writer.write_int_value("totalUpdateCount", self.total_update_count)
        writer.write_enum_value("updateCategory", self.update_category)
        writer.write_collection_of_object_values("updateStateSummaries", self.update_state_summaries)
        writer.write_str_value("userId", self.user_id)
    

