from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_integer_setting_value_default_template import DeviceManagementConfigurationIntegerSettingValueDefaultTemplate
    from .device_management_configuration_integer_setting_value_definition_template import DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate
    from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

@dataclass
class DeviceManagementConfigurationIntegerSettingValueTemplate(DeviceManagementConfigurationSimpleSettingValueTemplate, Parsable):
    """
    Integer Setting Value Template
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationIntegerSettingValueTemplate"
    # Integer Setting Value Default Template.
    default_value: Optional[DeviceManagementConfigurationIntegerSettingValueDefaultTemplate] = None
    # Recommended value definition.
    recommended_value_definition: Optional[DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None
    # Required value definition.
    required_value_definition: Optional[DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationIntegerSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationIntegerSettingValueTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationIntegerSettingValueTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_integer_setting_value_default_template import DeviceManagementConfigurationIntegerSettingValueDefaultTemplate
        from .device_management_configuration_integer_setting_value_definition_template import DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

        from .device_management_configuration_integer_setting_value_default_template import DeviceManagementConfigurationIntegerSettingValueDefaultTemplate
        from .device_management_configuration_integer_setting_value_definition_template import DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(DeviceManagementConfigurationIntegerSettingValueDefaultTemplate)),
            "recommendedValueDefinition": lambda n : setattr(self, 'recommended_value_definition', n.get_object_value(DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate)),
            "requiredValueDefinition": lambda n : setattr(self, 'required_value_definition', n.get_object_value(DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate)),
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
        writer.write_object_value("recommendedValueDefinition", self.recommended_value_definition)
        writer.write_object_value("requiredValueDefinition", self.required_value_definition)
    

