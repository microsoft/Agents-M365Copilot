from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_state import ActionState
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsInformationProtectionWipeAction(Entity, Parsable):
    """
    Represents wipe requests issued by tenant admin for Bring-Your-Own-Device(BYOD) Windows devices.
    """
    # Last checkin time of the device that was targeted by this wipe action.
    last_check_in_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ActionState] = None
    # Targeted device Mac address.
    targeted_device_mac_address: Optional[str] = None
    # Targeted device name.
    targeted_device_name: Optional[str] = None
    # The DeviceRegistrationId being targeted by this wipe action.
    targeted_device_registration_id: Optional[str] = None
    # The UserId being targeted by this wipe action.
    targeted_user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionWipeAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionWipeAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionWipeAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_state import ActionState
        from .entity import Entity

        from .action_state import ActionState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "lastCheckInDateTime": lambda n : setattr(self, 'last_check_in_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ActionState)),
            "targetedDeviceMacAddress": lambda n : setattr(self, 'targeted_device_mac_address', n.get_str_value()),
            "targetedDeviceName": lambda n : setattr(self, 'targeted_device_name', n.get_str_value()),
            "targetedDeviceRegistrationId": lambda n : setattr(self, 'targeted_device_registration_id', n.get_str_value()),
            "targetedUserId": lambda n : setattr(self, 'targeted_user_id', n.get_str_value()),
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
        writer.write_datetime_value("lastCheckInDateTime", self.last_check_in_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("targetedDeviceMacAddress", self.targeted_device_mac_address)
        writer.write_str_value("targetedDeviceName", self.targeted_device_name)
        writer.write_str_value("targetedDeviceRegistrationId", self.targeted_device_registration_id)
        writer.write_str_value("targetedUserId", self.targeted_user_id)
    

