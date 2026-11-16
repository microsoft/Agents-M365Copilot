from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate
    from .device_management_configuration_string_setting_value_default_template import DeviceManagementConfigurationStringSettingValueDefaultTemplate

from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

@dataclass
class DeviceManagementConfigurationStringSettingValueTemplate(DeviceManagementConfigurationSimpleSettingValueTemplate, Parsable):
    """
    String Setting Value Template
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationStringSettingValueTemplate"
    # String Setting Value Default Template.
    default_value: Optional[DeviceManagementConfigurationStringSettingValueDefaultTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationStringSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValueTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationStringSettingValueTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate
        from .device_management_configuration_string_setting_value_default_template import DeviceManagementConfigurationStringSettingValueDefaultTemplate

        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate
        from .device_management_configuration_string_setting_value_default_template import DeviceManagementConfigurationStringSettingValueDefaultTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(DeviceManagementConfigurationStringSettingValueDefaultTemplate)),
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
    

