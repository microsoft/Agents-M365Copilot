from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
    from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
    from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
    from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue
    from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition
    from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

@dataclass
class DeviceManagementConfigurationSimpleSettingDefinition(DeviceManagementConfigurationSettingDefinition, Parsable):
    # Default setting value for this setting.
    default_value: Optional[DeviceManagementConfigurationSettingValue] = None
    # list of child settings that depend on this setting.
    depended_on_by: Optional[list[DeviceManagementConfigurationSettingDependedOnBy]] = None
    # list of parent settings this setting is dependent on.
    dependent_on: Optional[list[DeviceManagementConfigurationDependentOn]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Definition of the value for this setting.
    value_definition: Optional[DeviceManagementConfigurationSettingValueDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSimpleSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition".casefold():
            from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

            return DeviceManagementConfigurationSimpleSettingCollectionDefinition()
        return DeviceManagementConfigurationSimpleSettingDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
        from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue
        from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition
        from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

        from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
        from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue
        from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition
        from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(DeviceManagementConfigurationSettingValue)),
            "dependedOnBy": lambda n : setattr(self, 'depended_on_by', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDependedOnBy)),
            "dependentOn": lambda n : setattr(self, 'dependent_on', n.get_collection_of_object_values(DeviceManagementConfigurationDependentOn)),
            "valueDefinition": lambda n : setattr(self, 'value_definition', n.get_object_value(DeviceManagementConfigurationSettingValueDefinition)),
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
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_collection_of_object_values("dependedOnBy", self.depended_on_by)
        writer.write_collection_of_object_values("dependentOn", self.dependent_on)
        writer.write_object_value("valueDefinition", self.value_definition)
    

