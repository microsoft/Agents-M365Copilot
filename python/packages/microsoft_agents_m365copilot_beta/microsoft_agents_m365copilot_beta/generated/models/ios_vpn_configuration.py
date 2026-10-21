from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_vpn_configuration import AppleVpnConfiguration
    from .app_list_item import AppListItem
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
    from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
    from .ios_certificate_profile_base import IosCertificateProfileBase

from .apple_vpn_configuration import AppleVpnConfiguration

@dataclass
class IosVpnConfiguration(AppleVpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the iOS device to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosVpnConfiguration"
    # Zscaler only. Zscaler cloud which the user is assigned to.
    cloud_name: Optional[str] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[DeviceManagementDerivedCredentialSettings] = None
    # Zscaler only. List of network addresses which are not sent through the Zscaler cloud.
    exclude_list: Optional[list[str]] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[IosCertificateProfileBase] = None
    # Microsoft Tunnel site ID.
    microsoft_tunnel_site_id: Optional[str] = None
    # Zscaler only. Blocks network traffic until the user signs into Zscaler app. 'True' means traffic is blocked.
    strict_enforcement: Optional[bool] = None
    # Targeted mobile apps. This collection can contain a maximum of 500 elements.
    targeted_mobile_apps: Optional[list[AppListItem]] = None
    # Zscaler only. Enter a static domain to pre-populate the login field with in the Zscaler app. If this is left empty, the user's Azure Active Directory domain will be used instead.
    user_domain: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosikEv2VpnConfiguration".casefold():
            from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration

            return IosikEv2VpnConfiguration()
        return IosVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .app_list_item import AppListItem
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .ios_certificate_profile_base import IosCertificateProfileBase

        from .apple_vpn_configuration import AppleVpnConfiguration
        from .app_list_item import AppListItem
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .ios_certificate_profile_base import IosCertificateProfileBase

        fields: dict[str, Callable[[Any], None]] = {
            "cloudName": lambda n : setattr(self, 'cloud_name', n.get_str_value()),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(DeviceManagementDerivedCredentialSettings)),
            "excludeList": lambda n : setattr(self, 'exclude_list', n.get_collection_of_primitive_values(str)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(IosCertificateProfileBase)),
            "microsoftTunnelSiteId": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "strictEnforcement": lambda n : setattr(self, 'strict_enforcement', n.get_bool_value()),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_object_values(AppListItem)),
            "userDomain": lambda n : setattr(self, 'user_domain', n.get_str_value()),
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
        writer.write_str_value("cloudName", self.cloud_name)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_collection_of_primitive_values("excludeList", self.exclude_list)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_bool_value("strictEnforcement", self.strict_enforcement)
        writer.write_collection_of_object_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_str_value("userDomain", self.user_domain)
    

