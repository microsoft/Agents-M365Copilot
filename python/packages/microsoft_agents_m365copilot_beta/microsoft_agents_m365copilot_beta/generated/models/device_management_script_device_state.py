from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .managed_device import ManagedDevice
    from .run_state import RunState

from .entity import Entity

@dataclass
class DeviceManagementScriptDeviceState(Entity, Parsable):
    """
    Contains properties for device run state of the device management script.
    """
    # Error code corresponding to erroneous execution of the device management script.
    error_code: Optional[int] = None
    # Error description corresponding to erroneous execution of the device management script.
    error_description: Optional[str] = None
    # Latest time the device management script executes.
    last_state_update_date_time: Optional[datetime.datetime] = None
    # The managed devices that executes the device management script.
    managed_device: Optional[ManagedDevice] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Details of execution output.
    result_message: Optional[str] = None
    # Indicates the type of execution status of the device management script.
    run_state: Optional[RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementScriptDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptDeviceState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementScriptDeviceState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .managed_device import ManagedDevice
        from .run_state import RunState

        from .entity import Entity
        from .managed_device import ManagedDevice
        from .run_state import RunState

        fields: dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "errorDescription": lambda n : setattr(self, 'error_description', n.get_str_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "managedDevice": lambda n : setattr(self, 'managed_device', n.get_object_value(ManagedDevice)),
            "resultMessage": lambda n : setattr(self, 'result_message', n.get_str_value()),
            "runState": lambda n : setattr(self, 'run_state', n.get_enum_value(RunState)),
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
        writer.write_int_value("errorCode", self.error_code)
        writer.write_str_value("errorDescription", self.error_description)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_object_value("managedDevice", self.managed_device)
        writer.write_str_value("resultMessage", self.result_message)
        writer.write_enum_value("runState", self.run_state)
    

