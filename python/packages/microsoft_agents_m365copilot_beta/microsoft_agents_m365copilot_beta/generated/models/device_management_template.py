from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_setting_instance import DeviceManagementSettingInstance
    from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
    from .device_management_template_subtype import DeviceManagementTemplateSubtype
    from .device_management_template_type import DeviceManagementTemplateType
    from .entity import Entity
    from .policy_platform_type import PolicyPlatformType
    from .security_baseline_template import SecurityBaselineTemplate

from .entity import Entity

@dataclass
class DeviceManagementTemplate(Entity, Parsable):
    """
    Entity that represents a defined collection of device settings
    """
    # Collection of setting categories within the template
    categories: Optional[list[DeviceManagementTemplateSettingCategory]] = None
    # The template's description
    description: Optional[str] = None
    # The template's display name
    display_name: Optional[str] = None
    # Number of Intents created from this template.
    intent_count: Optional[int] = None
    # The template is deprecated or not. Intents cannot be created from a deprecated template.
    is_deprecated: Optional[bool] = None
    # Collection of templates this template can migrate to
    migratable_to: Optional[list[DeviceManagementTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[PolicyPlatformType] = None
    # When the template was published
    published_date_time: Optional[datetime.datetime] = None
    # Collection of all settings this template has
    settings: Optional[list[DeviceManagementSettingInstance]] = None
    # Template subtype
    template_subtype: Optional[DeviceManagementTemplateSubtype] = None
    # Template type
    template_type: Optional[DeviceManagementTemplateType] = None
    # The template's version information
    version_info: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineTemplate".casefold():
            from .security_baseline_template import SecurityBaselineTemplate

            return SecurityBaselineTemplate()
        return DeviceManagementTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_setting_instance import DeviceManagementSettingInstance
        from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
        from .device_management_template_subtype import DeviceManagementTemplateSubtype
        from .device_management_template_type import DeviceManagementTemplateType
        from .entity import Entity
        from .policy_platform_type import PolicyPlatformType
        from .security_baseline_template import SecurityBaselineTemplate

        from .device_management_setting_instance import DeviceManagementSettingInstance
        from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
        from .device_management_template_subtype import DeviceManagementTemplateSubtype
        from .device_management_template_type import DeviceManagementTemplateType
        from .entity import Entity
        from .policy_platform_type import PolicyPlatformType
        from .security_baseline_template import SecurityBaselineTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(DeviceManagementTemplateSettingCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "intentCount": lambda n : setattr(self, 'intent_count', n.get_int_value()),
            "isDeprecated": lambda n : setattr(self, 'is_deprecated', n.get_bool_value()),
            "migratableTo": lambda n : setattr(self, 'migratable_to', n.get_collection_of_object_values(DeviceManagementTemplate)),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(PolicyPlatformType)),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(DeviceManagementSettingInstance)),
            "templateSubtype": lambda n : setattr(self, 'template_subtype', n.get_enum_value(DeviceManagementTemplateSubtype)),
            "templateType": lambda n : setattr(self, 'template_type', n.get_enum_value(DeviceManagementTemplateType)),
            "versionInfo": lambda n : setattr(self, 'version_info', n.get_str_value()),
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
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("intentCount", self.intent_count)
        writer.write_bool_value("isDeprecated", self.is_deprecated)
        writer.write_collection_of_object_values("migratableTo", self.migratable_to)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_enum_value("templateSubtype", self.template_subtype)
        writer.write_enum_value("templateType", self.template_type)
        writer.write_str_value("versionInfo", self.version_info)
    

