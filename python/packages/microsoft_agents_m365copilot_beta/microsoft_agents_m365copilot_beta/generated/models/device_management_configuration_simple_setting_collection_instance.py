from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance
    from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

@dataclass
class DeviceManagementConfigurationSimpleSettingCollectionInstance(DeviceManagementConfigurationSettingInstance, Parsable):
    """
    Simple setting collection instance
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance"
    # Simple setting collection instance value
    simple_setting_collection_value: Optional[list[DeviceManagementConfigurationSimpleSettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSimpleSettingCollectionInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingCollectionInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationSimpleSettingCollectionInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

        from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance
        from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue

        fields: dict[str, Callable[[Any], None]] = {
            "simpleSettingCollectionValue": lambda n : setattr(self, 'simple_setting_collection_value', n.get_collection_of_object_values(DeviceManagementConfigurationSimpleSettingValue)),
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
        writer.write_collection_of_object_values("simpleSettingCollectionValue", self.simple_setting_collection_value)
    

