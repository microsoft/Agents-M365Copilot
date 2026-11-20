from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_azure_ad_trust_type import DeviceManagementConfigurationAzureAdTrustType
    from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
    from .device_management_configuration_windows_skus import DeviceManagementConfigurationWindowsSkus

from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability

@dataclass
class DeviceManagementConfigurationWindowsSettingApplicability(DeviceManagementConfigurationSettingApplicability, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability"
    # Version of CSP setting is a part of
    configuration_service_provider_version: Optional[str] = None
    # Maximum supported version of Windows
    maximum_supported_version: Optional[str] = None
    # Minimum supported version of Windows
    minimum_supported_version: Optional[str] = None
    # Required AAD Trust Type
    required_azure_ad_trust_type: Optional[DeviceManagementConfigurationAzureAdTrustType] = None
    # AzureAD setting requirement
    requires_azure_ad: Optional[bool] = None
    # List of Windows SKUs that the setting is applicable for
    windows_skus: Optional[list[DeviceManagementConfigurationWindowsSkus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationWindowsSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationWindowsSettingApplicability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationWindowsSettingApplicability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_azure_ad_trust_type import DeviceManagementConfigurationAzureAdTrustType
        from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
        from .device_management_configuration_windows_skus import DeviceManagementConfigurationWindowsSkus

        from .device_management_configuration_azure_ad_trust_type import DeviceManagementConfigurationAzureAdTrustType
        from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
        from .device_management_configuration_windows_skus import DeviceManagementConfigurationWindowsSkus

        fields: dict[str, Callable[[Any], None]] = {
            "configurationServiceProviderVersion": lambda n : setattr(self, 'configuration_service_provider_version', n.get_str_value()),
            "maximumSupportedVersion": lambda n : setattr(self, 'maximum_supported_version', n.get_str_value()),
            "minimumSupportedVersion": lambda n : setattr(self, 'minimum_supported_version', n.get_str_value()),
            "requiredAzureAdTrustType": lambda n : setattr(self, 'required_azure_ad_trust_type', n.get_enum_value(DeviceManagementConfigurationAzureAdTrustType)),
            "requiresAzureAd": lambda n : setattr(self, 'requires_azure_ad', n.get_bool_value()),
            "windowsSkus": lambda n : setattr(self, 'windows_skus', n.get_collection_of_enum_values(DeviceManagementConfigurationWindowsSkus)),
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
        writer.write_str_value("configurationServiceProviderVersion", self.configuration_service_provider_version)
        writer.write_str_value("maximumSupportedVersion", self.maximum_supported_version)
        writer.write_str_value("minimumSupportedVersion", self.minimum_supported_version)
        writer.write_enum_value("requiredAzureAdTrustType", self.required_azure_ad_trust_type)
        writer.write_bool_value("requiresAzureAd", self.requires_azure_ad)
        writer.write_collection_of_enum_values("windowsSkus", self.windows_skus)
    

