from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_setting_instance import DeviceManagementSettingInstance

from .device_management_setting_instance import DeviceManagementSettingInstance

@dataclass
class DeviceManagementAbstractComplexSettingInstance(DeviceManagementSettingInstance, Parsable):
    """
    A setting instance representing a complex value for an abstract setting
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementAbstractComplexSettingInstance"
    # The definition ID for the chosen implementation of this complex setting
    implementation_id: Optional[str] = None
    # The values that make up the complex setting
    value: Optional[list[DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementAbstractComplexSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAbstractComplexSettingInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementAbstractComplexSettingInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_setting_instance import DeviceManagementSettingInstance

        from .device_management_setting_instance import DeviceManagementSettingInstance

        fields: dict[str, Callable[[Any], None]] = {
            "implementationId": lambda n : setattr(self, 'implementation_id', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(DeviceManagementSettingInstance)),
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
        writer.write_str_value("implementationId", self.implementation_id)
        writer.write_collection_of_object_values("value", self.value)
    

