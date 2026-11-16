from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition
    from .device_management_configuration_string_format import DeviceManagementConfigurationStringFormat

from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition

@dataclass
class DeviceManagementConfigurationStringSettingValueDefinition(DeviceManagementConfigurationSettingValueDefinition, Parsable):
    """
    String constraints
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationStringSettingValueDefinition"
    # Supported file types for this setting.
    file_types: Optional[list[str]] = None
    # Pre-defined format of the string. The possible values are: none, email, guid, ip, base64, url, version, xml, date, time, binary, regEx, json, dateTime, surfaceHub, bashScript, unknownFutureValue.
    format: Optional[DeviceManagementConfigurationStringFormat] = None
    # Regular expression or any xml or json schema that the input string should match
    input_validation_schema: Optional[str] = None
    # Specifies whether the setting needs to be treated as a secret. Settings marked as yes will be encrypted in transit and at rest and will be displayed as asterisks when represented in the UX.
    is_secret: Optional[bool] = None
    # Maximum length of string. Valid values 0 to 87516
    maximum_length: Optional[int] = None
    # Minimum length of string. Valid values 0 to 87516
    minimum_length: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationStringSettingValueDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValueDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationStringSettingValueDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition
        from .device_management_configuration_string_format import DeviceManagementConfigurationStringFormat

        from .device_management_configuration_setting_value_definition import DeviceManagementConfigurationSettingValueDefinition
        from .device_management_configuration_string_format import DeviceManagementConfigurationStringFormat

        fields: dict[str, Callable[[Any], None]] = {
            "fileTypes": lambda n : setattr(self, 'file_types', n.get_collection_of_primitive_values(str)),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(DeviceManagementConfigurationStringFormat)),
            "inputValidationSchema": lambda n : setattr(self, 'input_validation_schema', n.get_str_value()),
            "isSecret": lambda n : setattr(self, 'is_secret', n.get_bool_value()),
            "maximumLength": lambda n : setattr(self, 'maximum_length', n.get_int_value()),
            "minimumLength": lambda n : setattr(self, 'minimum_length', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("fileTypes", self.file_types)
        writer.write_enum_value("format", self.format)
        writer.write_str_value("inputValidationSchema", self.input_validation_schema)
        writer.write_bool_value("isSecret", self.is_secret)
        writer.write_int_value("maximumLength", self.maximum_length)
        writer.write_int_value("minimumLength", self.minimum_length)
    

