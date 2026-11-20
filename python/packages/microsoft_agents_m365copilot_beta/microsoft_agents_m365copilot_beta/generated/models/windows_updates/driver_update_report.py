from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .driver_update_device_status import DriverUpdateDeviceStatus

from ..entity import Entity

@dataclass
class DriverUpdateReport(Entity, Parsable):
    # The device class targeted by the driver update. Read-only.
    class_: Optional[str] = None
    # The latest rollout statuses for devices associated with the driver update.
    device_statuses: Optional[list[DriverUpdateDeviceStatus]] = None
    # The display name of the driver update. Read-only.
    display_name: Optional[str] = None
    # The manufacturer of the driver update. Read-only.
    manufacturer: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the driver update was released. Read-only.
    release_date_time: Optional[datetime.datetime] = None
    # The driver version. Read-only.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriverUpdateReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriverUpdateReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriverUpdateReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .driver_update_device_status import DriverUpdateDeviceStatus

        from ..entity import Entity
        from .driver_update_device_status import DriverUpdateDeviceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "class": lambda n : setattr(self, 'class_', n.get_str_value()),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(DriverUpdateDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
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
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
    

