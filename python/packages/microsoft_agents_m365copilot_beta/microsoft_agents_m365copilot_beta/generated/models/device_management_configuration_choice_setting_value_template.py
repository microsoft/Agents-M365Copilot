from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
    from .device_management_configuration_choice_setting_value_definition_template import DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate

@dataclass
class DeviceManagementConfigurationChoiceSettingValueTemplate(AdditionalDataHolder, Parsable):
    """
    Choice Setting Value Template
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Choice Setting Value Default Template.
    default_value: Optional[DeviceManagementConfigurationChoiceSettingValueDefaultTemplate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Recommended definition override.
    recommended_value_definition: Optional[DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = None
    # Required definition override.
    required_value_definition: Optional[DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = None
    # Setting Value Template Id
    setting_value_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationChoiceSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingValueTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationChoiceSettingValueTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
        from .device_management_configuration_choice_setting_value_definition_template import DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate

        from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
        from .device_management_configuration_choice_setting_value_definition_template import DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(DeviceManagementConfigurationChoiceSettingValueDefaultTemplate)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendedValueDefinition": lambda n : setattr(self, 'recommended_value_definition', n.get_object_value(DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate)),
            "requiredValueDefinition": lambda n : setattr(self, 'required_value_definition', n.get_object_value(DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate)),
            "settingValueTemplateId": lambda n : setattr(self, 'setting_value_template_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recommendedValueDefinition", self.recommended_value_definition)
        writer.write_object_value("requiredValueDefinition", self.required_value_definition)
        writer.write_str_value("settingValueTemplateId", self.setting_value_template_id)
        writer.write_additional_data_value(self.additional_data)
    

