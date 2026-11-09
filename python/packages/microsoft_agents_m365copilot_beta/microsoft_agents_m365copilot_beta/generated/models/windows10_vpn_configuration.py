from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cryptography_suite import CryptographySuite
    from .extended_key_usage import ExtendedKeyUsage
    from .vpn_dns_rule import VpnDnsRule
    from .vpn_route import VpnRoute
    from .vpn_traffic_rule import VpnTrafficRule
    from .windows10_associated_apps import Windows10AssociatedApps
    from .windows10_vpn_authentication_method import Windows10VpnAuthenticationMethod
    from .windows10_vpn_connection_type import Windows10VpnConnectionType
    from .windows10_vpn_profile_target import Windows10VpnProfileTarget
    from .windows10_vpn_proxy_server import Windows10VpnProxyServer
    from .windows_certificate_profile_base import WindowsCertificateProfileBase
    from .windows_vpn_configuration import WindowsVpnConfiguration

from .windows_vpn_configuration import WindowsVpnConfiguration

@dataclass
class Windows10VpnConfiguration(WindowsVpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Windows 10 device (desktop or mobile) to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10VpnConfiguration"
    # Associated Apps. This collection can contain a maximum of 10000 elements.
    associated_apps: Optional[list[Windows10AssociatedApps]] = None
    # Windows 10 VPN connection types.
    authentication_method: Optional[Windows10VpnAuthenticationMethod] = None
    # VPN connection types.
    connection_type: Optional[Windows10VpnConnectionType] = None
    # Cryptography Suite security settings for IKEv2 VPN in Windows10 and above
    cryptography_suite: Optional[CryptographySuite] = None
    # DNS rules. This collection can contain a maximum of 1000 elements.
    dns_rules: Optional[list[VpnDnsRule]] = None
    # Specify DNS suffixes to add to the DNS search list to properly route short names.
    dns_suffixes: Optional[list[str]] = None
    # Extensible Authentication Protocol (EAP) XML. (UTF8 encoded byte array)
    eap_xml: Optional[bytes] = None
    # Enable Always On mode.
    enable_always_on: Optional[bool] = None
    # Enable conditional access.
    enable_conditional_access: Optional[bool] = None
    # Enable device tunnel.
    enable_device_tunnel: Optional[bool] = None
    # Enable IP address registration with internal DNS.
    enable_dns_registration: Optional[bool] = None
    # Enable single sign-on (SSO) with alternate certificate.
    enable_single_sign_on_with_alternate_certificate: Optional[bool] = None
    # Enable split tunneling.
    enable_split_tunneling: Optional[bool] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[WindowsCertificateProfileBase] = None
    # ID of the Microsoft Tunnel site associated with the VPN profile.
    microsoft_tunnel_site_id: Optional[str] = None
    # Only associated Apps can use connection (per-app VPN).
    only_associated_apps_can_use_connection: Optional[bool] = None
    # Profile target type. Possible values are: user, device, autoPilotDevice.
    profile_target: Optional[Windows10VpnProfileTarget] = None
    # Proxy Server.
    proxy_server: Optional[Windows10VpnProxyServer] = None
    # Remember user credentials.
    remember_user_credentials: Optional[bool] = None
    # Routes (optional for third-party providers). This collection can contain a maximum of 1000 elements.
    routes: Optional[list[VpnRoute]] = None
    # Single sign-on Extended Key Usage (EKU).
    single_sign_on_eku: Optional[ExtendedKeyUsage] = None
    # Single sign-on issuer hash.
    single_sign_on_issuer_hash: Optional[str] = None
    # Traffic rules. This collection can contain a maximum of 1000 elements.
    traffic_rules: Optional[list[VpnTrafficRule]] = None
    # Trusted Network Domains
    trusted_network_domains: Optional[list[str]] = None
    # Windows Information Protection (WIP) domain to associate with this connection.
    windows_information_protection_domain: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10VpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10VpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cryptography_suite import CryptographySuite
        from .extended_key_usage import ExtendedKeyUsage
        from .vpn_dns_rule import VpnDnsRule
        from .vpn_route import VpnRoute
        from .vpn_traffic_rule import VpnTrafficRule
        from .windows10_associated_apps import Windows10AssociatedApps
        from .windows10_vpn_authentication_method import Windows10VpnAuthenticationMethod
        from .windows10_vpn_connection_type import Windows10VpnConnectionType
        from .windows10_vpn_profile_target import Windows10VpnProfileTarget
        from .windows10_vpn_proxy_server import Windows10VpnProxyServer
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_vpn_configuration import WindowsVpnConfiguration

        from .cryptography_suite import CryptographySuite
        from .extended_key_usage import ExtendedKeyUsage
        from .vpn_dns_rule import VpnDnsRule
        from .vpn_route import VpnRoute
        from .vpn_traffic_rule import VpnTrafficRule
        from .windows10_associated_apps import Windows10AssociatedApps
        from .windows10_vpn_authentication_method import Windows10VpnAuthenticationMethod
        from .windows10_vpn_connection_type import Windows10VpnConnectionType
        from .windows10_vpn_profile_target import Windows10VpnProfileTarget
        from .windows10_vpn_proxy_server import Windows10VpnProxyServer
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_vpn_configuration import WindowsVpnConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "associatedApps": lambda n : setattr(self, 'associated_apps', n.get_collection_of_object_values(Windows10AssociatedApps)),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(Windows10VpnAuthenticationMethod)),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(Windows10VpnConnectionType)),
            "cryptographySuite": lambda n : setattr(self, 'cryptography_suite', n.get_object_value(CryptographySuite)),
            "dnsRules": lambda n : setattr(self, 'dns_rules', n.get_collection_of_object_values(VpnDnsRule)),
            "dnsSuffixes": lambda n : setattr(self, 'dns_suffixes', n.get_collection_of_primitive_values(str)),
            "eapXml": lambda n : setattr(self, 'eap_xml', n.get_bytes_value()),
            "enableAlwaysOn": lambda n : setattr(self, 'enable_always_on', n.get_bool_value()),
            "enableConditionalAccess": lambda n : setattr(self, 'enable_conditional_access', n.get_bool_value()),
            "enableDeviceTunnel": lambda n : setattr(self, 'enable_device_tunnel', n.get_bool_value()),
            "enableDnsRegistration": lambda n : setattr(self, 'enable_dns_registration', n.get_bool_value()),
            "enableSingleSignOnWithAlternateCertificate": lambda n : setattr(self, 'enable_single_sign_on_with_alternate_certificate', n.get_bool_value()),
            "enableSplitTunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(WindowsCertificateProfileBase)),
            "microsoftTunnelSiteId": lambda n : setattr(self, 'microsoft_tunnel_site_id', n.get_str_value()),
            "onlyAssociatedAppsCanUseConnection": lambda n : setattr(self, 'only_associated_apps_can_use_connection', n.get_bool_value()),
            "profileTarget": lambda n : setattr(self, 'profile_target', n.get_enum_value(Windows10VpnProfileTarget)),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(Windows10VpnProxyServer)),
            "rememberUserCredentials": lambda n : setattr(self, 'remember_user_credentials', n.get_bool_value()),
            "routes": lambda n : setattr(self, 'routes', n.get_collection_of_object_values(VpnRoute)),
            "singleSignOnEku": lambda n : setattr(self, 'single_sign_on_eku', n.get_object_value(ExtendedKeyUsage)),
            "singleSignOnIssuerHash": lambda n : setattr(self, 'single_sign_on_issuer_hash', n.get_str_value()),
            "trafficRules": lambda n : setattr(self, 'traffic_rules', n.get_collection_of_object_values(VpnTrafficRule)),
            "trustedNetworkDomains": lambda n : setattr(self, 'trusted_network_domains', n.get_collection_of_primitive_values(str)),
            "windowsInformationProtectionDomain": lambda n : setattr(self, 'windows_information_protection_domain', n.get_str_value()),
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
        writer.write_collection_of_object_values("associatedApps", self.associated_apps)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_object_value("cryptographySuite", self.cryptography_suite)
        writer.write_collection_of_object_values("dnsRules", self.dns_rules)
        writer.write_collection_of_primitive_values("dnsSuffixes", self.dns_suffixes)
        writer.write_bytes_value("eapXml", self.eap_xml)
        writer.write_bool_value("enableAlwaysOn", self.enable_always_on)
        writer.write_bool_value("enableConditionalAccess", self.enable_conditional_access)
        writer.write_bool_value("enableDeviceTunnel", self.enable_device_tunnel)
        writer.write_bool_value("enableDnsRegistration", self.enable_dns_registration)
        writer.write_bool_value("enableSingleSignOnWithAlternateCertificate", self.enable_single_sign_on_with_alternate_certificate)
        writer.write_bool_value("enableSplitTunneling", self.enable_split_tunneling)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("microsoftTunnelSiteId", self.microsoft_tunnel_site_id)
        writer.write_bool_value("onlyAssociatedAppsCanUseConnection", self.only_associated_apps_can_use_connection)
        writer.write_enum_value("profileTarget", self.profile_target)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_bool_value("rememberUserCredentials", self.remember_user_credentials)
        writer.write_collection_of_object_values("routes", self.routes)
        writer.write_object_value("singleSignOnEku", self.single_sign_on_eku)
        writer.write_str_value("singleSignOnIssuerHash", self.single_sign_on_issuer_hash)
        writer.write_collection_of_object_values("trafficRules", self.traffic_rules)
        writer.write_collection_of_primitive_values("trustedNetworkDomains", self.trusted_network_domains)
        writer.write_str_value("windowsInformationProtectionDomain", self.windows_information_protection_domain)
    

