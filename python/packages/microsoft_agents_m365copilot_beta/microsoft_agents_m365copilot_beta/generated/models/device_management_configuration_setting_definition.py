from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
    from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
    from .device_management_configuration_control_type import DeviceManagementConfigurationControlType
    from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
    from .device_management_configuration_referred_setting_information import DeviceManagementConfigurationReferredSettingInformation
    from .device_management_configuration_setting_access_types import DeviceManagementConfigurationSettingAccessTypes
    from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
    from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
    from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
    from .device_management_configuration_setting_occurrence import DeviceManagementConfigurationSettingOccurrence
    from .device_management_configuration_setting_risk_level import DeviceManagementConfigurationSettingRiskLevel
    from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
    from .device_management_configuration_setting_visibility import DeviceManagementConfigurationSettingVisibility
    from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
    from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementConfigurationSettingDefinition(Entity, Parsable):
    # The accessTypes property
    access_types: Optional[DeviceManagementConfigurationSettingAccessTypes] = None
    # Details which device setting is applicable on. Supports: $filters.
    applicability: Optional[DeviceManagementConfigurationSettingApplicability] = None
    # Base CSP Path
    base_uri: Optional[str] = None
    # Specify category in which the setting is under. Support $filters.
    category_id: Optional[str] = None
    # Description of the setting.
    description: Optional[str] = None
    # Name of the setting. For example: Allow Toast.
    display_name: Optional[str] = None
    # Help text of the setting. Give more details of the setting.
    help_text: Optional[str] = None
    # List of links more info for the setting can be found at.
    info_urls: Optional[list[str]] = None
    # Tokens which to search settings on
    keywords: Optional[list[str]] = None
    # Name of the item
    name: Optional[str] = None
    # Indicates whether the setting is required or not
    occurrence: Optional[DeviceManagementConfigurationSettingOccurrence] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Offset CSP Path from Base
    offset_uri: Optional[str] = None
    # List of referred setting information.
    referred_setting_information_list: Optional[list[DeviceManagementConfigurationReferredSettingInformation]] = None
    # Setting RiskLevel
    risk_level: Optional[DeviceManagementConfigurationSettingRiskLevel] = None
    # Root setting definition id if the setting is a child setting.
    root_definition_id: Optional[str] = None
    # Supported setting types
    setting_usage: Optional[DeviceManagementConfigurationSettingUsage] = None
    # Setting control type representation in the UX
    ux_behavior: Optional[DeviceManagementConfigurationControlType] = None
    # Item Version
    version: Optional[str] = None
    # Supported setting types
    visibility: Optional[DeviceManagementConfigurationSettingVisibility] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingDefinition
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingDefinition".casefold():
            from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition

            return DeviceManagementConfigurationChoiceSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationRedirectSettingDefinition".casefold():
            from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition

            return DeviceManagementConfigurationRedirectSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionDefinition".casefold():
            from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition

            return DeviceManagementConfigurationSettingGroupCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupDefinition".casefold():
            from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition

            return DeviceManagementConfigurationSettingGroupDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition".casefold():
            from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

            return DeviceManagementConfigurationSimpleSettingCollectionDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingDefinition".casefold():
            from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition

            return DeviceManagementConfigurationSimpleSettingDefinition()
        return DeviceManagementConfigurationSettingDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
        from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
        from .device_management_configuration_control_type import DeviceManagementConfigurationControlType
        from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
        from .device_management_configuration_referred_setting_information import DeviceManagementConfigurationReferredSettingInformation
        from .device_management_configuration_setting_access_types import DeviceManagementConfigurationSettingAccessTypes
        from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
        from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
        from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
        from .device_management_configuration_setting_occurrence import DeviceManagementConfigurationSettingOccurrence
        from .device_management_configuration_setting_risk_level import DeviceManagementConfigurationSettingRiskLevel
        from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
        from .device_management_configuration_setting_visibility import DeviceManagementConfigurationSettingVisibility
        from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
        from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
        from .entity import Entity

        from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
        from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
        from .device_management_configuration_control_type import DeviceManagementConfigurationControlType
        from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
        from .device_management_configuration_referred_setting_information import DeviceManagementConfigurationReferredSettingInformation
        from .device_management_configuration_setting_access_types import DeviceManagementConfigurationSettingAccessTypes
        from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
        from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
        from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
        from .device_management_configuration_setting_occurrence import DeviceManagementConfigurationSettingOccurrence
        from .device_management_configuration_setting_risk_level import DeviceManagementConfigurationSettingRiskLevel
        from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
        from .device_management_configuration_setting_visibility import DeviceManagementConfigurationSettingVisibility
        from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
        from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessTypes": lambda n : setattr(self, 'access_types', n.get_collection_of_enum_values(DeviceManagementConfigurationSettingAccessTypes)),
            "applicability": lambda n : setattr(self, 'applicability', n.get_object_value(DeviceManagementConfigurationSettingApplicability)),
            "baseUri": lambda n : setattr(self, 'base_uri', n.get_str_value()),
            "categoryId": lambda n : setattr(self, 'category_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "helpText": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "infoUrls": lambda n : setattr(self, 'info_urls', n.get_collection_of_primitive_values(str)),
            "keywords": lambda n : setattr(self, 'keywords', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "occurrence": lambda n : setattr(self, 'occurrence', n.get_object_value(DeviceManagementConfigurationSettingOccurrence)),
            "offsetUri": lambda n : setattr(self, 'offset_uri', n.get_str_value()),
            "referredSettingInformationList": lambda n : setattr(self, 'referred_setting_information_list', n.get_collection_of_object_values(DeviceManagementConfigurationReferredSettingInformation)),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_collection_of_enum_values(DeviceManagementConfigurationSettingRiskLevel)),
            "rootDefinitionId": lambda n : setattr(self, 'root_definition_id', n.get_str_value()),
            "settingUsage": lambda n : setattr(self, 'setting_usage', n.get_collection_of_enum_values(DeviceManagementConfigurationSettingUsage)),
            "uxBehavior": lambda n : setattr(self, 'ux_behavior', n.get_enum_value(DeviceManagementConfigurationControlType)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_collection_of_enum_values(DeviceManagementConfigurationSettingVisibility)),
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
        writer.write_enum_value("accessTypes", self.access_types)
        writer.write_object_value("applicability", self.applicability)
        writer.write_str_value("baseUri", self.base_uri)
        writer.write_str_value("categoryId", self.category_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_collection_of_primitive_values("infoUrls", self.info_urls)
        writer.write_collection_of_primitive_values("keywords", self.keywords)
        writer.write_str_value("name", self.name)
        writer.write_object_value("occurrence", self.occurrence)
        writer.write_str_value("offsetUri", self.offset_uri)
        writer.write_collection_of_object_values("referredSettingInformationList", self.referred_setting_information_list)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_str_value("rootDefinitionId", self.root_definition_id)
        writer.write_enum_value("settingUsage", self.setting_usage)
        writer.write_enum_value("uxBehavior", self.ux_behavior)
        writer.write_str_value("version", self.version)
        writer.write_enum_value("visibility", self.visibility)
    

