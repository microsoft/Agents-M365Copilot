from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_app_management_task import DeviceAppManagementTask
    from .endpoint_security_configuration_applicable_platform import EndpointSecurityConfigurationApplicablePlatform
    from .endpoint_security_configuration_profile_type import EndpointSecurityConfigurationProfileType
    from .endpoint_security_configuration_type import EndpointSecurityConfigurationType
    from .key_value_pair import KeyValuePair
    from .vulnerable_managed_device import VulnerableManagedDevice

from .device_app_management_task import DeviceAppManagementTask

@dataclass
class SecurityConfigurationTask(DeviceAppManagementTask, Parsable):
    """
    A security configuration task.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.securityConfigurationTask"
    # The endpoint security configuration applicable platform.
    applicable_platform: Optional[EndpointSecurityConfigurationApplicablePlatform] = None
    # The endpoint security policy type.
    endpoint_security_policy: Optional[EndpointSecurityConfigurationType] = None
    # The endpoint security policy profile type.
    endpoint_security_policy_profile: Optional[EndpointSecurityConfigurationProfileType] = None
    # Information about the mitigation.
    insights: Optional[str] = None
    # The intended settings and their values.
    intended_settings: Optional[list[KeyValuePair]] = None
    # The number of vulnerable devices.
    managed_device_count: Optional[int] = None
    # The vulnerable managed devices.
    managed_devices: Optional[list[VulnerableManagedDevice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityConfigurationTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityConfigurationTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityConfigurationTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_app_management_task import DeviceAppManagementTask
        from .endpoint_security_configuration_applicable_platform import EndpointSecurityConfigurationApplicablePlatform
        from .endpoint_security_configuration_profile_type import EndpointSecurityConfigurationProfileType
        from .endpoint_security_configuration_type import EndpointSecurityConfigurationType
        from .key_value_pair import KeyValuePair
        from .vulnerable_managed_device import VulnerableManagedDevice

        from .device_app_management_task import DeviceAppManagementTask
        from .endpoint_security_configuration_applicable_platform import EndpointSecurityConfigurationApplicablePlatform
        from .endpoint_security_configuration_profile_type import EndpointSecurityConfigurationProfileType
        from .endpoint_security_configuration_type import EndpointSecurityConfigurationType
        from .key_value_pair import KeyValuePair
        from .vulnerable_managed_device import VulnerableManagedDevice

        fields: dict[str, Callable[[Any], None]] = {
            "applicablePlatform": lambda n : setattr(self, 'applicable_platform', n.get_enum_value(EndpointSecurityConfigurationApplicablePlatform)),
            "endpointSecurityPolicy": lambda n : setattr(self, 'endpoint_security_policy', n.get_enum_value(EndpointSecurityConfigurationType)),
            "endpointSecurityPolicyProfile": lambda n : setattr(self, 'endpoint_security_policy_profile', n.get_enum_value(EndpointSecurityConfigurationProfileType)),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "intendedSettings": lambda n : setattr(self, 'intended_settings', n.get_collection_of_object_values(KeyValuePair)),
            "managedDeviceCount": lambda n : setattr(self, 'managed_device_count', n.get_int_value()),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(VulnerableManagedDevice)),
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
        writer.write_enum_value("applicablePlatform", self.applicable_platform)
        writer.write_enum_value("endpointSecurityPolicy", self.endpoint_security_policy)
        writer.write_enum_value("endpointSecurityPolicyProfile", self.endpoint_security_policy_profile)
        writer.write_str_value("insights", self.insights)
        writer.write_collection_of_object_values("intendedSettings", self.intended_settings)
        writer.write_int_value("managedDeviceCount", self.managed_device_count)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
    

