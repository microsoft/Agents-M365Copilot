from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_apple_applicability_constraint import DeviceManagementConfigurationAppleApplicabilityConstraint
    from .device_management_configuration_apple_applicability_device_type import DeviceManagementConfigurationAppleApplicabilityDeviceType
    from .device_management_configuration_apple_o_s_supported_versions import DeviceManagementConfigurationAppleOSSupportedVersions

@dataclass
class DeviceManagementConfigurationAppleSettingVersionApplicability(AdditionalDataHolder, Parsable):
    """
    Represents the applicable versions for an Apple setting.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the supported channel types for an Apple setting.
    constraints: Optional[DeviceManagementConfigurationAppleApplicabilityConstraint] = None
    # Indicates the supported device type for an apple setting.
    device_type: Optional[DeviceManagementConfigurationAppleApplicabilityDeviceType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the version range for an apple setting.
    supported_versions: Optional[DeviceManagementConfigurationAppleOSSupportedVersions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationAppleSettingVersionApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationAppleSettingVersionApplicability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationAppleSettingVersionApplicability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_apple_applicability_constraint import DeviceManagementConfigurationAppleApplicabilityConstraint
        from .device_management_configuration_apple_applicability_device_type import DeviceManagementConfigurationAppleApplicabilityDeviceType
        from .device_management_configuration_apple_o_s_supported_versions import DeviceManagementConfigurationAppleOSSupportedVersions

        from .device_management_configuration_apple_applicability_constraint import DeviceManagementConfigurationAppleApplicabilityConstraint
        from .device_management_configuration_apple_applicability_device_type import DeviceManagementConfigurationAppleApplicabilityDeviceType
        from .device_management_configuration_apple_o_s_supported_versions import DeviceManagementConfigurationAppleOSSupportedVersions

        fields: dict[str, Callable[[Any], None]] = {
            "constraints": lambda n : setattr(self, 'constraints', n.get_collection_of_enum_values(DeviceManagementConfigurationAppleApplicabilityConstraint)),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_collection_of_enum_values(DeviceManagementConfigurationAppleApplicabilityDeviceType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportedVersions": lambda n : setattr(self, 'supported_versions', n.get_object_value(DeviceManagementConfigurationAppleOSSupportedVersions)),
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
        writer.write_enum_value("constraints", self.constraints)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("supportedVersions", self.supported_versions)
        writer.write_additional_data_value(self.additional_data)
    

