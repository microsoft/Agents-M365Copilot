from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementScriptRunSummary(Entity, Parsable):
    """
    Contains properties for the run summary of a device management script.
    """
    # Error device count.
    error_device_count: Optional[int] = None
    # Error user count.
    error_user_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Success device count.
    success_device_count: Optional[int] = None
    # Success user count.
    success_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementScriptRunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptRunSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementScriptRunSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "errorUserCount": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "successDeviceCount": lambda n : setattr(self, 'success_device_count', n.get_int_value()),
            "successUserCount": lambda n : setattr(self, 'success_user_count', n.get_int_value()),
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
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("errorUserCount", self.error_user_count)
        writer.write_int_value("successDeviceCount", self.success_device_count)
        writer.write_int_value("successUserCount", self.success_user_count)
    

