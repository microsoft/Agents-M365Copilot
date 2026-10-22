from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
    from .device_management_configuration_option_definition import DeviceManagementConfigurationOptionDefinition
    from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

@dataclass
class DeviceManagementConfigurationChoiceSettingDefinition(DeviceManagementConfigurationSettingDefinition, Parsable):
    # Default option for the choice setting.
    default_option_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Options for the setting that can be selected.
    options: Optional[list[DeviceManagementConfigurationOptionDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationChoiceSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionDefinition".casefold():
            from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition

            return DeviceManagementConfigurationChoiceSettingCollectionDefinition()
        return DeviceManagementConfigurationChoiceSettingDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
        from .device_management_configuration_option_definition import DeviceManagementConfigurationOptionDefinition
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

        from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
        from .device_management_configuration_option_definition import DeviceManagementConfigurationOptionDefinition
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "defaultOptionId": lambda n : setattr(self, 'default_option_id', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(DeviceManagementConfigurationOptionDefinition)),
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
        writer.write_str_value("defaultOptionId", self.default_option_id)
        writer.write_collection_of_object_values("options", self.options)
    

