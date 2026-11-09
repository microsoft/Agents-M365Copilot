from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .run_state import RunState

from .entity import Entity

@dataclass
class HardwareConfigurationDeviceState(Entity, Parsable):
    """
    Contains properties for device run state of the hardware configuration
    """
    # A list of identifier strings of different assignment filters applied
    assignment_filter_ids: Optional[str] = None
    # Error from the hardware configuration execution
    configuration_error: Optional[str] = None
    # Output of the hardware configuration execution
    configuration_output: Optional[str] = None
    # Indicates the type of execution status of the device management script.
    configuration_state: Optional[RunState] = None
    # The name of the device
    device_name: Optional[str] = None
    # The Policy internal version
    internal_version: Optional[int] = None
    # The last timestamp of when the hardware configuration executed
    last_state_update_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating system version of the device (E.g. 10.0.19042.1165, 10.0.19042.1288 etc.)
    os_version: Optional[str] = None
    # User Principal Name (UPN).
    upn: Optional[str] = None
    # The unique identifier of the Entra user associated with the device for which policy is applied. Read-Only.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwareConfigurationDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareConfigurationDeviceState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwareConfigurationDeviceState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .run_state import RunState

        from .entity import Entity
        from .run_state import RunState

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentFilterIds": lambda n : setattr(self, 'assignment_filter_ids', n.get_str_value()),
            "configurationError": lambda n : setattr(self, 'configuration_error', n.get_str_value()),
            "configurationOutput": lambda n : setattr(self, 'configuration_output', n.get_str_value()),
            "configurationState": lambda n : setattr(self, 'configuration_state', n.get_enum_value(RunState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "internalVersion": lambda n : setattr(self, 'internal_version', n.get_int_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
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
        writer.write_str_value("assignmentFilterIds", self.assignment_filter_ids)
        writer.write_str_value("configurationError", self.configuration_error)
        writer.write_str_value("configurationOutput", self.configuration_output)
        writer.write_enum_value("configurationState", self.configuration_state)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_int_value("internalVersion", self.internal_version)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("upn", self.upn)
        writer.write_str_value("userId", self.user_id)
    

