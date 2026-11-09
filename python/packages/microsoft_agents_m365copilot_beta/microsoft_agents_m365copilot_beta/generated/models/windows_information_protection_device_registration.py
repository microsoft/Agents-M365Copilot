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
class WindowsInformationProtectionDeviceRegistration(Entity, Parsable):
    """
    Represents device registration records for Bring-Your-Own-Device(BYOD) Windows devices.
    """
    # Device Mac address.
    device_mac_address: Optional[str] = None
    # Device name.
    device_name: Optional[str] = None
    # Device identifier for this device registration record.
    device_registration_id: Optional[str] = None
    # Device type, for example, Windows laptop VS Windows phone.
    device_type: Optional[str] = None
    # Last checkin time of the device.
    last_check_in_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # UserId associated with this device registration record.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionDeviceRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionDeviceRegistration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionDeviceRegistration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceMacAddress": lambda n : setattr(self, 'device_mac_address', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceRegistrationId": lambda n : setattr(self, 'device_registration_id', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "lastCheckInDateTime": lambda n : setattr(self, 'last_check_in_date_time', n.get_datetime_value()),
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
        writer.write_str_value("deviceMacAddress", self.device_mac_address)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceRegistrationId", self.device_registration_id)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_datetime_value("lastCheckInDateTime", self.last_check_in_date_time)
        writer.write_str_value("userId", self.user_id)
    

