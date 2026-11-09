from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily

@dataclass
class DeviceManagementConfigurationPolicyTemplateReference(AdditionalDataHolder, Parsable):
    """
    Policy template reference information
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Template Display Name of the referenced template. This property is read-only.
    template_display_name: Optional[str] = None
    # Template Display Version of the referenced Template. This property is read-only.
    template_display_version: Optional[str] = None
    # Describes the TemplateFamily for the Template entity
    template_family: Optional[DeviceManagementConfigurationTemplateFamily] = None
    # Template id
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationPolicyTemplateReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicyTemplateReference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationPolicyTemplateReference()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily

        from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "templateDisplayName": lambda n : setattr(self, 'template_display_name', n.get_str_value()),
            "templateDisplayVersion": lambda n : setattr(self, 'template_display_version', n.get_str_value()),
            "templateFamily": lambda n : setattr(self, 'template_family', n.get_enum_value(DeviceManagementConfigurationTemplateFamily)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("templateFamily", self.template_family)
        writer.write_str_value("templateId", self.template_id)
        writer.write_additional_data_value(self.additional_data)
    

