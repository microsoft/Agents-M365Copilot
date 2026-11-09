from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vpn_authentication_method import VpnAuthenticationMethod
    from .windows81_vpn_configuration import Windows81VpnConfiguration
    from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

from .windows81_vpn_configuration import Windows81VpnConfiguration

@dataclass
class WindowsPhone81VpnConfiguration(Windows81VpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Windows Phone 8.1 to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81VpnConfiguration"
    # VPN Authentication Method.
    authentication_method: Optional[VpnAuthenticationMethod] = None
    # Bypass VPN on company Wi-Fi.
    bypass_vpn_on_company_wifi: Optional[bool] = None
    # Bypass VPN on home Wi-Fi.
    bypass_vpn_on_home_wifi: Optional[bool] = None
    # DNS suffix search list.
    dns_suffix_search_list: Optional[list[str]] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[WindowsPhone81CertificateProfileBase] = None
    # Remember user credentials.
    remember_user_credentials: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPhone81VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81VpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhone81VpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

        from .vpn_authentication_method import VpnAuthenticationMethod
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(VpnAuthenticationMethod)),
            "bypassVpnOnCompanyWifi": lambda n : setattr(self, 'bypass_vpn_on_company_wifi', n.get_bool_value()),
            "bypassVpnOnHomeWifi": lambda n : setattr(self, 'bypass_vpn_on_home_wifi', n.get_bool_value()),
            "dnsSuffixSearchList": lambda n : setattr(self, 'dns_suffix_search_list', n.get_collection_of_primitive_values(str)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(WindowsPhone81CertificateProfileBase)),
            "rememberUserCredentials": lambda n : setattr(self, 'remember_user_credentials', n.get_bool_value()),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_bool_value("bypassVpnOnCompanyWifi", self.bypass_vpn_on_company_wifi)
        writer.write_bool_value("bypassVpnOnHomeWifi", self.bypass_vpn_on_home_wifi)
        writer.write_collection_of_primitive_values("dnsSuffixSearchList", self.dns_suffix_search_list)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("rememberUserCredentials", self.remember_user_credentials)
    

