from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_constraint import DeviceManagementConstraint

from .device_management_constraint import DeviceManagementConstraint

@dataclass
class DeviceManagementSettingAbstractImplementationConstraint(DeviceManagementConstraint, Parsable):
    """
    Constraint that enforces an AbstractComplex type has or is set to a particular value
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint"
    # List of value which means not configured for the setting
    allowed_abstract_implementation_definition_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingAbstractImplementationConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingAbstractImplementationConstraint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettingAbstractImplementationConstraint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_constraint import DeviceManagementConstraint

        from .device_management_constraint import DeviceManagementConstraint

        fields: dict[str, Callable[[Any], None]] = {
            "allowedAbstractImplementationDefinitionIds": lambda n : setattr(self, 'allowed_abstract_implementation_definition_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedAbstractImplementationDefinitionIds", self.allowed_abstract_implementation_definition_ids)
    

