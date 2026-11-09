from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_script_device_state import DeviceManagementScriptDeviceState
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementScriptUserState(Entity, Parsable):
    """
    Contains properties for user run state of the device management script.
    """
    # List of run states for this script across all devices of specific user.
    device_run_states: Optional[list[DeviceManagementScriptDeviceState]] = None
    # Error device count for specific user.
    error_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Success device count for specific user.
    success_device_count: Optional[int] = None
    # User principle name of specific user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementScriptUserState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptUserState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementScriptUserState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_script_device_state import DeviceManagementScriptDeviceState
        from .entity import Entity

        from .device_management_script_device_state import DeviceManagementScriptDeviceState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(DeviceManagementScriptDeviceState)),
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "successDeviceCount": lambda n : setattr(self, 'success_device_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("successDeviceCount", self.success_device_count)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

