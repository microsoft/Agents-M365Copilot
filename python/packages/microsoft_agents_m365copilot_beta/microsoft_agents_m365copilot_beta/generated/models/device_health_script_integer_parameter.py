from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_health_script_parameter import DeviceHealthScriptParameter

from .device_health_script_parameter import DeviceHealthScriptParameter

@dataclass
class DeviceHealthScriptIntegerParameter(DeviceHealthScriptParameter, Parsable):
    """
    Properties of the  Integer script parameter.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceHealthScriptIntegerParameter"
    # The default value of Integer param. Valid values -2147483648 to 2147483647
    default_value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptIntegerParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptIntegerParameter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptIntegerParameter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_health_script_parameter import DeviceHealthScriptParameter

        from .device_health_script_parameter import DeviceHealthScriptParameter

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_int_value()),
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
        writer.write_int_value("defaultValue", self.default_value)
    

