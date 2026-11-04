from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_app_credential_provider_role_state import AndroidAppCredentialProviderRoleState
    from .android_permission_action import AndroidPermissionAction
    from .android_profile_applicability import AndroidProfileApplicability
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

@dataclass
class AndroidForWorkMobileAppConfiguration(ManagedDeviceMobileAppConfiguration, Parsable):
    """
    Contains properties, inherited properties and actions for AFW mobile app configurations.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkMobileAppConfiguration"
    # Setting to specify whether to allow ConnectedApps experience for this app.
    connected_apps_enabled: Optional[bool] = None
    # The Android credential provider role state for apps.
    credential_provider_role_state: Optional[AndroidAppCredentialProviderRoleState] = None
    # Android For Work app configuration package id.
    package_id: Optional[str] = None
    # Android For Work app configuration JSON payload.
    payload_json: Optional[str] = None
    # List of Android app permissions and corresponding permission actions.
    permission_actions: Optional[list[AndroidPermissionAction]] = None
    # Android profile applicability
    profile_applicability: Optional[AndroidProfileApplicability] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkMobileAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkMobileAppConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkMobileAppConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_app_credential_provider_role_state import AndroidAppCredentialProviderRoleState
        from .android_permission_action import AndroidPermissionAction
        from .android_profile_applicability import AndroidProfileApplicability
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        from .android_app_credential_provider_role_state import AndroidAppCredentialProviderRoleState
        from .android_permission_action import AndroidPermissionAction
        from .android_profile_applicability import AndroidProfileApplicability
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "connectedAppsEnabled": lambda n : setattr(self, 'connected_apps_enabled', n.get_bool_value()),
            "credentialProviderRoleState": lambda n : setattr(self, 'credential_provider_role_state', n.get_enum_value(AndroidAppCredentialProviderRoleState)),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "payloadJson": lambda n : setattr(self, 'payload_json', n.get_str_value()),
            "permissionActions": lambda n : setattr(self, 'permission_actions', n.get_collection_of_object_values(AndroidPermissionAction)),
            "profileApplicability": lambda n : setattr(self, 'profile_applicability', n.get_enum_value(AndroidProfileApplicability)),
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
        writer.write_bool_value("connectedAppsEnabled", self.connected_apps_enabled)
        writer.write_enum_value("credentialProviderRoleState", self.credential_provider_role_state)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("payloadJson", self.payload_json)
        writer.write_collection_of_object_values("permissionActions", self.permission_actions)
        writer.write_enum_value("profileApplicability", self.profile_applicability)
    

