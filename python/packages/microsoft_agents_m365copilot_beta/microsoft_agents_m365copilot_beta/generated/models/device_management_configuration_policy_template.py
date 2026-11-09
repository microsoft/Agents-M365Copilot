from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
    from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
    from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
    from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily
    from .device_management_template_lifecycle_state import DeviceManagementTemplateLifecycleState
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementConfigurationPolicyTemplate(Entity, Parsable):
    """
    Device Management Configuration Policy Template
    """
    # Allow unmanaged setting templates
    allow_unmanaged_settings: Optional[bool] = None
    # Template base identifier
    base_id: Optional[str] = None
    # Template description
    description: Optional[str] = None
    # Indicates whether assignments to Entra security groups is disabled
    disable_entra_group_policy_assignment: Optional[bool] = None
    # Template display name
    display_name: Optional[str] = None
    # Description of template version
    display_version: Optional[str] = None
    # Describes current lifecycle state of a template
    lifecycle_state: Optional[DeviceManagementTemplateLifecycleState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types.
    platforms: Optional[DeviceManagementConfigurationPlatforms] = None
    # Number of setting templates. Valid values 0 to 2147483647. This property is read-only.
    setting_template_count: Optional[int] = None
    # Setting templates
    setting_templates: Optional[list[DeviceManagementConfigurationSettingTemplate]] = None
    # Describes which technology this setting can be deployed with
    technologies: Optional[DeviceManagementConfigurationTechnologies] = None
    # Describes the TemplateFamily for the Template entity
    template_family: Optional[DeviceManagementConfigurationTemplateFamily] = None
    # Template version. Valid values 1 to 2147483647. This property is read-only.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationPolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicyTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationPolicyTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
        from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
        from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
        from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily
        from .device_management_template_lifecycle_state import DeviceManagementTemplateLifecycleState
        from .entity import Entity

        from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
        from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
        from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
        from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily
        from .device_management_template_lifecycle_state import DeviceManagementTemplateLifecycleState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allowUnmanagedSettings": lambda n : setattr(self, 'allow_unmanaged_settings', n.get_bool_value()),
            "baseId": lambda n : setattr(self, 'base_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disableEntraGroupPolicyAssignment": lambda n : setattr(self, 'disable_entra_group_policy_assignment', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "displayVersion": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "lifecycleState": lambda n : setattr(self, 'lifecycle_state', n.get_enum_value(DeviceManagementTemplateLifecycleState)),
            "platforms": lambda n : setattr(self, 'platforms', n.get_collection_of_enum_values(DeviceManagementConfigurationPlatforms)),
            "settingTemplateCount": lambda n : setattr(self, 'setting_template_count', n.get_int_value()),
            "settingTemplates": lambda n : setattr(self, 'setting_templates', n.get_collection_of_object_values(DeviceManagementConfigurationSettingTemplate)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_collection_of_enum_values(DeviceManagementConfigurationTechnologies)),
            "templateFamily": lambda n : setattr(self, 'template_family', n.get_enum_value(DeviceManagementConfigurationTemplateFamily)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bool_value("allowUnmanagedSettings", self.allow_unmanaged_settings)
        writer.write_str_value("baseId", self.base_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("disableEntraGroupPolicyAssignment", self.disable_entra_group_policy_assignment)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_enum_value("lifecycleState", self.lifecycle_state)
        writer.write_enum_value("platforms", self.platforms)
        writer.write_collection_of_object_values("settingTemplates", self.setting_templates)
        writer.write_enum_value("technologies", self.technologies)
        writer.write_enum_value("templateFamily", self.template_family)
    

