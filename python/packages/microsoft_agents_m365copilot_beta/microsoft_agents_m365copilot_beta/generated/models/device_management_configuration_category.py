from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
    from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
    from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementConfigurationCategory(Entity, Parsable):
    """
    Device Management Configuration Policy
    """
    # Description of the category header in policy summary.
    category_description: Optional[str] = None
    # List of child ids of the category.
    child_category_ids: Optional[list[str]] = None
    # Description of the category. For example: Display
    description: Optional[str] = None
    # Name of the category. For example: Device Lock
    display_name: Optional[str] = None
    # Help text of the category. Give more details of the category.
    help_text: Optional[str] = None
    # Name of the item
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Direct parent id of the category. If the category is the root, the parent id is same as its id.
    parent_category_id: Optional[str] = None
    # Supported platform types.
    platforms: Optional[DeviceManagementConfigurationPlatforms] = None
    # Root id of the category.
    root_category_id: Optional[str] = None
    # Supported setting types
    setting_usage: Optional[DeviceManagementConfigurationSettingUsage] = None
    # Describes which technology this setting can be deployed with
    technologies: Optional[DeviceManagementConfigurationTechnologies] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
        from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
        from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
        from .entity import Entity

        from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
        from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
        from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "categoryDescription": lambda n : setattr(self, 'category_description', n.get_str_value()),
            "childCategoryIds": lambda n : setattr(self, 'child_category_ids', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "helpText": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentCategoryId": lambda n : setattr(self, 'parent_category_id', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_collection_of_enum_values(DeviceManagementConfigurationPlatforms)),
            "rootCategoryId": lambda n : setattr(self, 'root_category_id', n.get_str_value()),
            "settingUsage": lambda n : setattr(self, 'setting_usage', n.get_collection_of_enum_values(DeviceManagementConfigurationSettingUsage)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_collection_of_enum_values(DeviceManagementConfigurationTechnologies)),
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
        writer.write_str_value("categoryDescription", self.category_description)
        writer.write_collection_of_primitive_values("childCategoryIds", self.child_category_ids)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_str_value("name", self.name)
        writer.write_str_value("parentCategoryId", self.parent_category_id)
        writer.write_enum_value("platforms", self.platforms)
        writer.write_str_value("rootCategoryId", self.root_category_id)
        writer.write_enum_value("settingUsage", self.setting_usage)
        writer.write_enum_value("technologies", self.technologies)
    

