from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .managed_device_reported_app import ManagedDeviceReportedApp
    from .policy_platform_type import PolicyPlatformType
    from .restricted_apps_state import RestrictedAppsState

from .entity import Entity

@dataclass
class RestrictedAppsViolation(Entity, Parsable):
    """
    Violation of restricted apps configuration profile per device per user
    """
    # Device configuration profile unique identifier, must be Guid
    device_configuration_id: Optional[str] = None
    # Device configuration profile name
    device_configuration_name: Optional[str] = None
    # Device name
    device_name: Optional[str] = None
    # Managed device unique identifier, must be Guid
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[PolicyPlatformType] = None
    # List of violated restricted apps
    restricted_apps: Optional[list[ManagedDeviceReportedApp]] = None
    # Restricted apps state
    restricted_apps_state: Optional[RestrictedAppsState] = None
    # User unique identifier, must be Guid
    user_id: Optional[str] = None
    # User name
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestrictedAppsViolation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestrictedAppsViolation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestrictedAppsViolation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .managed_device_reported_app import ManagedDeviceReportedApp
        from .policy_platform_type import PolicyPlatformType
        from .restricted_apps_state import RestrictedAppsState

        from .entity import Entity
        from .managed_device_reported_app import ManagedDeviceReportedApp
        from .policy_platform_type import PolicyPlatformType
        from .restricted_apps_state import RestrictedAppsState

        fields: dict[str, Callable[[Any], None]] = {
            "deviceConfigurationId": lambda n : setattr(self, 'device_configuration_id', n.get_str_value()),
            "deviceConfigurationName": lambda n : setattr(self, 'device_configuration_name', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(PolicyPlatformType)),
            "restrictedApps": lambda n : setattr(self, 'restricted_apps', n.get_collection_of_object_values(ManagedDeviceReportedApp)),
            "restrictedAppsState": lambda n : setattr(self, 'restricted_apps_state', n.get_enum_value(RestrictedAppsState)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("deviceConfigurationId", self.device_configuration_id)
        writer.write_str_value("deviceConfigurationName", self.device_configuration_name)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_collection_of_object_values("restrictedApps", self.restricted_apps)
        writer.write_enum_value("restrictedAppsState", self.restricted_apps_state)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
    

