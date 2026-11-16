from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_constraint import DeviceManagementConstraint
    from .device_management_enum_value import DeviceManagementEnumValue

from .device_management_constraint import DeviceManagementConstraint

@dataclass
class DeviceManagementEnumConstraint(DeviceManagementConstraint, Parsable):
    """
    Constraint that enforces the setting value is from a permitted set of strings
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementEnumConstraint"
    # List of valid values for this string
    values: Optional[list[DeviceManagementEnumValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementEnumConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementEnumConstraint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementEnumConstraint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_constraint import DeviceManagementConstraint
        from .device_management_enum_value import DeviceManagementEnumValue

        from .device_management_constraint import DeviceManagementConstraint
        from .device_management_enum_value import DeviceManagementEnumValue

        fields: dict[str, Callable[[Any], None]] = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(DeviceManagementEnumValue)),
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
        writer.write_collection_of_object_values("values", self.values)
    

