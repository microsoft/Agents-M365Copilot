from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_constraint import DeviceManagementConstraint

from .device_management_constraint import DeviceManagementConstraint

@dataclass
class DeviceManagementSettingIntegerConstraint(DeviceManagementConstraint, Parsable):
    """
    Constraint enforcing the permitted value range for an integer setting
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementSettingIntegerConstraint"
    # The maximum permitted value
    maximum_value: Optional[int] = None
    # The minimum permitted value
    minimum_value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingIntegerConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingIntegerConstraint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettingIntegerConstraint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_constraint import DeviceManagementConstraint

        from .device_management_constraint import DeviceManagementConstraint

        fields: dict[str, Callable[[Any], None]] = {
            "maximumValue": lambda n : setattr(self, 'maximum_value', n.get_int_value()),
            "minimumValue": lambda n : setattr(self, 'minimum_value', n.get_int_value()),
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
        writer.write_int_value("maximumValue", self.maximum_value)
        writer.write_int_value("minimumValue", self.minimum_value)
    

