from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
    from .android_vpn_connection_type import AndroidVpnConnectionType
    from .app_list_item import AppListItem
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
    from .key_value import KeyValue
    from .key_value_pair import KeyValuePair
    from .vpn_configuration import VpnConfiguration
    from .vpn_proxy_server import VpnProxyServer

from .vpn_configuration import VpnConfiguration

@dataclass
class AndroidDeviceOwnerVpnConfiguration(VpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Android Fully Managed device to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerVpnConfiguration"
    # Whether or not to enable always-on VPN connection.
    always_on: Optional[bool] = None
    # If always-on VPN connection is enabled, whether or not to lock network traffic when that VPN is disconnected.
    always_on_lockdown: Optional[bool] = None
    # Android VPN connection type.
    connection_type: Optional[AndroidVpnConnectionType] = None
    # Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
    custom_data: Optional[list[KeyValue]] = None
    # Custom data to define key/value pairs specific to a VPN provider. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[list[KeyValuePair]] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[DeviceManagementDerivedCredentialSettings] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[AndroidDeviceOwnerCertificateProfileBase] = None
    # List of app package names that will be able to access the network directly when VPN is in lockdown mode but not connected.
    lockdown_exclusion_list: Optional[list[str]] = None
    # Microsoft Tunnel site ID.
    microsoft_tunnel_site_id: Optional[str] = None
    # List of hosts to exclude using the proxy on connections for. These hosts can use wildcards such as .example.com.
    proxy_exclusion_list: Optional[list[str]] = None
    # Proxy server.
    proxy_server: Optional[VpnProxyServer] = None
    # Targeted mobile apps. This collection can contain a maximum of 500 elements.
    targeted_mobile_apps: Optional[list[AppListItem]] = None
    # Targeted App package IDs.
    targeted_package_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerVpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_vpn_connection_type import AndroidVpnConnectionType
        from .app_list_item import AppListItem
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .vpn_configuration import VpnConfiguration
        from .vpn_proxy_server import VpnProxyServer

        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_vpn_connection_type import AndroidVpnConnectionType
        from .app_list_item import AppListItem
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .vpn_configuration import VpnConfiguration
        from .vpn_proxy_server import VpnProxyServer

        fields: dict[str, Callable[[Any], None]] = {
            "alwaysOn": lambda n : setattr(self, 'always_on', n.get_bool_value()),
            "alwaysOnLockdown": lambda n : setattr(self, 'always_on_lockdown', n.get_bool_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(AndroidVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(KeyValuePair)),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(DeviceManagementDerivedCredentialSettings)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(AndroidDeviceOwnerCertificateProfileBase)),
            "lockdownExclusionList": lambda n : setattr(self, 'lockdown_exclusion_list', n.get_collection_of_primitive_values(str)),
            "microsoftTunnelSiteId": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "proxyExclusionList": lambda n : setattr(self, 'proxy_exclusion_list', n.get_collection_of_primitive_values(str)),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(VpnProxyServer)),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(AppListItem)),
            "targetedPackageIds": lambda n : setattr(self, 'targeted_package_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("alwaysOn", self.always_on)
        writer.write_bool_value("alwaysOnLockdown", self.always_on_lockdown)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_collection_of_primitive_values("lockdownExclusionList", self.lockdown_exclusion_list)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_collection_of_primitive_values("proxyExclusionList", self.proxy_exclusion_list)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_collection_of_primitive_values("targetedPackageIds", self.targeted_package_ids)
    

