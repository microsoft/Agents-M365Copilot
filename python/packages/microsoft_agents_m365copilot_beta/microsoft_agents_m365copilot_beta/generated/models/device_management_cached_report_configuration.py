from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_report_status import DeviceManagementReportStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementCachedReportConfiguration(Entity, Parsable):
    """
    Entity representing the configuration of a cached report.
    """
    # Time that the cached report expires.
    expiration_date_time: Optional[datetime.datetime] = None
    # Filters applied on report creation.
    filter: Optional[str] = None
    # Time that the cached report was last refreshed.
    last_refresh_date_time: Optional[datetime.datetime] = None
    # Caller-managed metadata associated with the report.
    metadata: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Ordering of columns in the report.
    order_by: Optional[list[str]] = None
    # Name of the report.
    report_name: Optional[str] = None
    # Columns selected from the report.
    select: Optional[list[str]] = None
    # Possible statuses associated with a generated report.
    status: Optional[DeviceManagementReportStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementCachedReportConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementCachedReportConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementCachedReportConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_report_status import DeviceManagementReportStatus
        from .entity import Entity

        from .device_management_report_status import DeviceManagementReportStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "lastRefreshDateTime": lambda n : setattr(self, 'last_refresh_date_time', n.get_datetime_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "orderBy": lambda n : setattr(self, 'order_by', n.get_collection_of_primitive_values(str)),
            "reportName": lambda n : setattr(self, 'report_name', n.get_str_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DeviceManagementReportStatus)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("filter", self.filter)
        writer.write_datetime_value("lastRefreshDateTime", self.last_refresh_date_time)
        writer.write_str_value("metadata", self.metadata)
        writer.write_collection_of_primitive_values("orderBy", self.order_by)
        writer.write_str_value("reportName", self.report_name)
        writer.write_collection_of_primitive_values("select", self.select)
        writer.write_enum_value("status", self.status)
    

