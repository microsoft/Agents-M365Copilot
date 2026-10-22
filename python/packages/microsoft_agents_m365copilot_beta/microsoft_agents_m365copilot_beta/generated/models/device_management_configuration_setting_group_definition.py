from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
    from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
    from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
    from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition

from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

@dataclass
class DeviceManagementConfigurationSettingGroupDefinition(DeviceManagementConfigurationSettingDefinition, Parsable):
    # Dependent child settings to this group of settings.
    child_ids: Optional[list[str]] = None
    # List of child settings that depend on this setting
    depended_on_by: Optional[list[DeviceManagementConfigurationSettingDependedOnBy]] = None
    # List of Dependencies for the setting group
    dependent_on: Optional[list[DeviceManagementConfigurationDependentOn]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSettingGroupDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingGroupDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionDefinition".casefold():
            from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition

            return DeviceManagementConfigurationSettingGroupCollectionDefinition()
        return DeviceManagementConfigurationSettingGroupDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
        from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition

        from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
        from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "childIds": lambda n : setattr(self, 'child_ids', n.get_collection_of_primitive_values(str)),
            "dependedOnBy": lambda n : setattr(self, 'depended_on_by', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDependedOnBy)),
            "dependentOn": lambda n : setattr(self, 'dependent_on', n.get_collection_of_object_values(DeviceManagementConfigurationDependentOn)),
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
        writer.write_collection_of_primitive_values("childIds", self.child_ids)
        writer.write_collection_of_object_values("dependedOnBy", self.depended_on_by)
        writer.write_collection_of_object_values("dependentOn", self.dependent_on)
    

