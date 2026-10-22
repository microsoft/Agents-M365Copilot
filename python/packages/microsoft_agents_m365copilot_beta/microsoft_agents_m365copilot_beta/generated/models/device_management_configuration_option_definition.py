from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
    from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
    from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue

@dataclass
class DeviceManagementConfigurationOptionDefinition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # List of Settings that depends on this option
    depended_on_by: Optional[list[DeviceManagementConfigurationSettingDependedOnBy]] = None
    # List of dependent settings for this option
    dependent_on: Optional[list[DeviceManagementConfigurationDependentOn]] = None
    # Description of the option
    description: Optional[str] = None
    # Friendly name of the option
    display_name: Optional[str] = None
    # Help text of the option
    help_text: Optional[str] = None
    # Identifier of option
    item_id: Optional[str] = None
    # Name of the option
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Value of the option
    option_value: Optional[DeviceManagementConfigurationSettingValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationOptionDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationOptionDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationOptionDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
        from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
        from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue

        from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
        from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
        from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue

        fields: dict[str, Callable[[Any], None]] = {
            "dependedOnBy": lambda n : setattr(self, 'depended_on_by', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDependedOnBy)),
            "dependentOn": lambda n : setattr(self, 'dependent_on', n.get_collection_of_object_values(DeviceManagementConfigurationDependentOn)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "helpText": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "optionValue": lambda n : setattr(self, 'option_value', n.get_object_value(DeviceManagementConfigurationSettingValue)),
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
        writer.write_collection_of_object_values("dependedOnBy", self.depended_on_by)
        writer.write_collection_of_object_values("dependentOn", self.dependent_on)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("optionValue", self.option_value)
        writer.write_additional_data_value(self.additional_data)
    

