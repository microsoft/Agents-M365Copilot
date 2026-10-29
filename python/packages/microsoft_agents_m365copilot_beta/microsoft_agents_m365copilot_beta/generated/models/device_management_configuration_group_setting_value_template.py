from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

@dataclass
class DeviceManagementConfigurationGroupSettingValueTemplate(AdditionalDataHolder, Parsable):
    """
    Group Setting Value Template
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Group setting value children
    children: Optional[list[DeviceManagementConfigurationSettingInstanceTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Setting Value Template Id
    setting_value_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationGroupSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingValueTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationGroupSettingValueTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(DeviceManagementConfigurationSettingInstanceTemplate)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("settingValueTemplateId", self.setting_value_template_id)
        writer.write_additional_data_value(self.additional_data)
    

