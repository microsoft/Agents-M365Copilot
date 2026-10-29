from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
    from .device_management_setting_definition import DeviceManagementSettingDefinition
    from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementSettingCategory(Entity, Parsable):
    """
    Entity representing a setting category
    """
    # The category name
    display_name: Optional[str] = None
    # The category contains top level required setting
    has_required_setting: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The setting definitions this category contains
    setting_definitions: Optional[list[DeviceManagementSettingDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentSettingCategory".casefold():
            from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory

            return DeviceManagementIntentSettingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTemplateSettingCategory".casefold():
            from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory

            return DeviceManagementTemplateSettingCategory()
        return DeviceManagementSettingCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
        from .device_management_setting_definition import DeviceManagementSettingDefinition
        from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
        from .entity import Entity

        from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
        from .device_management_setting_definition import DeviceManagementSettingDefinition
        from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hasRequiredSetting": lambda n : setattr(self, 'has_required_setting', n.get_bool_value()),
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(DeviceManagementSettingDefinition)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hasRequiredSetting", self.has_required_setting)
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
    

