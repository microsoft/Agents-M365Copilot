from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .driver_approval_status import DriverApprovalStatus
    from .driver_category import DriverCategory
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsDriverUpdateInventory(Entity, Parsable):
    """
    A new entity to represent driver inventories.
    """
    # The number of devices for which this driver is applicable.
    applicable_device_count: Optional[int] = None
    # An enum type to represent approval status of a driver.
    approval_status: Optional[DriverApprovalStatus] = None
    # An enum type to represent which category a driver belongs to.
    category: Optional[DriverCategory] = None
    # The date time when a driver should be deployed if approvalStatus is approved.
    deploy_date_time: Optional[datetime.datetime] = None
    # The class of the driver.
    driver_class: Optional[str] = None
    # The manufacturer of the driver.
    manufacturer: Optional[str] = None
    # The name of the driver.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The release date time of the driver.
    release_date_time: Optional[datetime.datetime] = None
    # The version of the driver.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDriverUpdateInventory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDriverUpdateInventory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDriverUpdateInventory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .driver_approval_status import DriverApprovalStatus
        from .driver_category import DriverCategory
        from .entity import Entity

        from .driver_approval_status import DriverApprovalStatus
        from .driver_category import DriverCategory
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "applicableDeviceCount": lambda n : setattr(self, 'applicable_device_count', n.get_int_value()),
            "approvalStatus": lambda n : setattr(self, 'approval_status', n.get_enum_value(DriverApprovalStatus)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(DriverCategory)),
            "deployDateTime": lambda n : setattr(self, 'deploy_date_time', n.get_datetime_value()),
            "driverClass": lambda n : setattr(self, 'driver_class', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_int_value("applicableDeviceCount", self.applicable_device_count)
        writer.write_enum_value("approvalStatus", self.approval_status)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("deployDateTime", self.deploy_date_time)
        writer.write_str_value("driverClass", self.driver_class)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("name", self.name)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_str_value("version", self.version)
    

