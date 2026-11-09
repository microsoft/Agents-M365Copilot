from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_apple_setting_version_applicability import DeviceManagementConfigurationAppleSettingVersionApplicability
    from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability

from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability

@dataclass
class DeviceManagementConfigurationIosSettingApplicability(DeviceManagementConfigurationSettingApplicability, Parsable):
    """
    Indicates the applicability for an apple setting.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationIosSettingApplicability"
    # Gets a list of Apple applicability objects.
    version_applicabilities: Optional[list[DeviceManagementConfigurationAppleSettingVersionApplicability]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationIosSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationIosSettingApplicability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationIosSettingApplicability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_apple_setting_version_applicability import DeviceManagementConfigurationAppleSettingVersionApplicability
        from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability

        from .device_management_configuration_apple_setting_version_applicability import DeviceManagementConfigurationAppleSettingVersionApplicability
        from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability

        fields: dict[str, Callable[[Any], None]] = {
            "versionApplicabilities": lambda n : setattr(self, 'version_applicabilities', n.get_collection_of_object_values(DeviceManagementConfigurationAppleSettingVersionApplicability)),
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
        writer.write_collection_of_object_values("versionApplicabilities", self.version_applicabilities)
    

