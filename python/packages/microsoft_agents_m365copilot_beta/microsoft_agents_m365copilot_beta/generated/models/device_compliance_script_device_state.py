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
class DeviceComplianceScriptDeviceState(Entity, Parsable):
    """
    Contains properties for device run state of the device compliance script.
    """
    # Indicates the type of execution status of the device management script.
    detection_state: Optional[RunState] = None
    # The next timestamp of when the device compliance script is expected to execute
    expected_state_update_date_time: Optional[datetime.datetime] = None
    # The last timestamp of when the device compliance script executed
    last_state_update_date_time: Optional[datetime.datetime] = None
    # The last time that Intune Managment Extension synced with Intune
    last_sync_date_time: Optional[datetime.datetime] = None
    # The managed device on which the device compliance script executed
    managed_device: Optional[ManagedDevice] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Error from the detection script
    script_error: Optional[str] = None
    # Output of the detection script
    script_output: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceScriptDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptDeviceState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScriptDeviceState()
    
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
            "detectionState": lambda n : setattr(self, 'detection_state', n.get_enum_value(RunState)),
            "expectedStateUpdateDateTime": lambda n : setattr(self, 'expected_state_update_date_time', n.get_datetime_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managedDevice": lambda n : setattr(self, 'managed_device', n.get_object_value(ManagedDevice)),
            "scriptError": lambda n : setattr(self, 'script_error', n.get_str_value()),
            "scriptOutput": lambda n : setattr(self, 'script_output', n.get_str_value()),
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
        writer.write_enum_value("detectionState", self.detection_state)
        writer.write_datetime_value("expectedStateUpdateDateTime", self.expected_state_update_date_time)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_object_value("managedDevice", self.managed_device)
        writer.write_str_value("scriptError", self.script_error)
        writer.write_str_value("scriptOutput", self.script_output)
    

