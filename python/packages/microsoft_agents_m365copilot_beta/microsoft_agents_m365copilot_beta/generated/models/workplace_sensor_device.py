from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workplace_sensor import WorkplaceSensor

from .entity import Entity

@dataclass
class WorkplaceSensorDevice(Entity, Parsable):
    # The description of the device.
    description: Optional[str] = None
    # The user-defined unique identifier of the device provided at the time of creation.
    device_id: Optional[str] = None
    # The display name of the device.
    display_name: Optional[str] = None
    # The IPv4 address of the device.
    ip_v4_address: Optional[str] = None
    # The IPv6 address of the device.
    ip_v6_address: Optional[str] = None
    # The MAC address of the device.
    mac_address: Optional[str] = None
    # The manufacturer of the device.
    manufacturer: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the place where the device is located. If the device is installed in a room equipped with a mailbox, this property should match the ExternalDirectoryObjectId or Microsoft Entra object ID of the room mailbox.
    place_id: Optional[str] = None
    # A list of sensors associated with the device that collect and report data about physical or environmental conditions, such as occupancy, people count, inferred occupancy, temperature, Wi-Fi, and more.
    sensors: Optional[list[WorkplaceSensor]] = None
    # A list of custom tags associated with the device.
    tags: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkplaceSensorDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkplaceSensorDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkplaceSensorDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workplace_sensor import WorkplaceSensor

        from .entity import Entity
        from .workplace_sensor import WorkplaceSensor

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ipV4Address": lambda n : setattr(self, 'ip_v4_address', n.get_str_value()),
            "ipV6Address": lambda n : setattr(self, 'ip_v6_address', n.get_str_value()),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
            "sensors": lambda n : setattr(self, 'sensors', n.get_collection_of_object_values(WorkplaceSensor)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("ipV4Address", self.ip_v4_address)
        writer.write_str_value("ipV6Address", self.ip_v6_address)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("placeId", self.place_id)
        writer.write_collection_of_object_values("sensors", self.sensors)
        writer.write_collection_of_primitive_values("tags", self.tags)
    

