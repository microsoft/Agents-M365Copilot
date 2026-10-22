from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
    from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
    from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
    from .device_management_constraint import DeviceManagementConstraint
    from .device_management_setting_dependency import DeviceManagementSettingDependency
    from .device_manangement_intent_value_type import DeviceManangementIntentValueType
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementSettingDefinition(Entity, Parsable):
    """
    Entity representing the defintion for a given setting
    """
    # Collection of constraints for the setting value
    constraints: Optional[list[DeviceManagementConstraint]] = None
    # Collection of dependencies on other settings
    dependencies: Optional[list[DeviceManagementSettingDependency]] = None
    # The setting's description
    description: Optional[str] = None
    # The setting's display name
    display_name: Optional[str] = None
    # Url to setting documentation
    documentation_url: Optional[str] = None
    # subtitle of the setting header for more details about the category/section
    header_subtitle: Optional[str] = None
    # title of the setting header represents a category/section of a setting/settings
    header_title: Optional[str] = None
    # If the setting is top level, it can be configured without the need to be wrapped in a collection or complex setting
    is_top_level: Optional[bool] = None
    # Keywords associated with the setting
    keywords: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Placeholder text as an example of valid input
    placeholder_text: Optional[str] = None
    # The valueType property
    value_type: Optional[DeviceManangementIntentValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementAbstractComplexSettingDefinition".casefold():
            from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition

            return DeviceManagementAbstractComplexSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCollectionSettingDefinition".casefold():
            from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition

            return DeviceManagementCollectionSettingDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementComplexSettingDefinition".casefold():
            from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition

            return DeviceManagementComplexSettingDefinition()
        return DeviceManagementSettingDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
        from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
        from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
        from .device_management_constraint import DeviceManagementConstraint
        from .device_management_setting_dependency import DeviceManagementSettingDependency
        from .device_manangement_intent_value_type import DeviceManangementIntentValueType
        from .entity import Entity

        from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
        from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
        from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
        from .device_management_constraint import DeviceManagementConstraint
        from .device_management_setting_dependency import DeviceManagementSettingDependency
        from .device_manangement_intent_value_type import DeviceManangementIntentValueType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "constraints": lambda n : setattr(self, 'constraints', n.get_collection_of_object_values(DeviceManagementConstraint)),
            "dependencies": lambda n : setattr(self, 'dependencies', n.get_collection_of_object_values(DeviceManagementSettingDependency)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "documentationUrl": lambda n : setattr(self, 'documentation_url', n.get_str_value()),
            "headerSubtitle": lambda n : setattr(self, 'header_subtitle', n.get_str_value()),
            "headerTitle": lambda n : setattr(self, 'header_title', n.get_str_value()),
            "isTopLevel": lambda n : setattr(self, 'is_top_level', n.get_bool_value()),
            "keywords": lambda n : setattr(self, 'keywords', n.get_collection_of_primitive_values(str)),
            "placeholderText": lambda n : setattr(self, 'placeholder_text', n.get_str_value()),
            "valueType": lambda n : setattr(self, 'value_type', n.get_enum_value(DeviceManangementIntentValueType)),
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
        writer.write_collection_of_object_values("constraints", self.constraints)
        writer.write_collection_of_object_values("dependencies", self.dependencies)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("documentationUrl", self.documentation_url)
        writer.write_str_value("headerSubtitle", self.header_subtitle)
        writer.write_str_value("headerTitle", self.header_title)
        writer.write_bool_value("isTopLevel", self.is_top_level)
        writer.write_collection_of_primitive_values("keywords", self.keywords)
        writer.write_str_value("placeholderText", self.placeholder_text)
        writer.write_enum_value("valueType", self.value_type)
    

