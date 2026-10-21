from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_vpn_connection_type import AppleVpnConnectionType
    from .device_configuration import DeviceConfiguration
    from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
    from .ios_vpn_configuration import IosVpnConfiguration
    from .key_value import KeyValue
    from .key_value_pair import KeyValuePair
    from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
    from .vpn_authentication_method import VpnAuthenticationMethod
    from .vpn_on_demand_rule import VpnOnDemandRule
    from .vpn_provider_type import VpnProviderType
    from .vpn_proxy_server import VpnProxyServer
    from .vpn_server import VpnServer

from .device_configuration import DeviceConfiguration

@dataclass
class AppleVpnConfiguration(DeviceConfiguration, Parsable):
    """
    Apple VPN configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.appleVpnConfiguration"
    # Associated Domains
    associated_domains: Optional[list[str]] = None
    # VPN Authentication Method.
    authentication_method: Optional[VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Apple VPN connection type.
    connection_type: Optional[AppleVpnConnectionType] = None
    # Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
    custom_data: Optional[list[KeyValue]] = None
    # Custom data when connection type is set to Custom VPN. Use this field to enable functionality not supported by Intune, but available in your VPN solution. Contact your VPN vendor to learn how to add these key/value pairs. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[list[KeyValuePair]] = None
    # Toggle to prevent user from disabling automatic VPN in the Settings app
    disable_on_demand_user_override: Optional[bool] = None
    # Whether to disconnect after on-demand connection idles
    disconnect_on_idle: Optional[bool] = None
    # The length of time in seconds to wait before disconnecting an on-demand connection. Valid values 0 to 65535
    disconnect_on_idle_timer_in_seconds: Optional[int] = None
    # Setting this to true creates Per-App VPN payload which can later be associated with Apps that can trigger this VPN conneciton on the end user's iOS device.
    enable_per_app: Optional[bool] = None
    # Send all network traffic through VPN.
    enable_split_tunneling: Optional[bool] = None
    # Indicates whether local network traffic is excluded from the VPN tunnel. When TRUE, local network traffic bypasses the VPN tunnel. Default value is null. Only takes effect when includeAllNetworks is TRUE or enforceVpnRouting is TRUE. Not applicable when enablePerApp is TRUE.
    exclude_local_networks: Optional[bool] = None
    # Domains that are accessed through the public internet instead of through VPN, even when per-app VPN is activated
    excluded_domains: Optional[list[str]] = None
    # Identifier provided by VPN vendor when connection type is set to Custom VPN. For example: Cisco AnyConnect uses an identifier of the form com.cisco.anyconnect.applevpn.plugin
    identifier: Optional[str] = None
    # Indicates whether most network traffic is routed through the VPN tunnel. When TRUE, most network traffic is sent through the VPN tunnel. Default value is null. Not applicable when enablePerApp is TRUE.
    include_all_networks: Optional[bool] = None
    # Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
    login_group_or_domain: Optional[str] = None
    # On-Demand Rules. This collection can contain a maximum of 500 elements.
    on_demand_rules: Optional[list[VpnOnDemandRule]] = None
    # Opt-In to sharing the device's Id to third-party vpn clients for use during network access control validation.
    opt_in_to_device_id_sharing: Optional[bool] = None
    # Provider type for per-app VPN. Possible values are: notConfigured, appProxy, packetTunnel.
    provider_type: Optional[VpnProviderType] = None
    # Proxy Server.
    proxy_server: Optional[VpnProxyServer] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # Safari domains when this VPN per App setting is enabled. In addition to the apps associated with this VPN, Safari domains specified here will also be able to trigger this VPN connection.
    safari_domains: Optional[list[str]] = None
    # VPN Server definition.
    server: Optional[VpnServer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppleVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleVpnConfiguration
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVpnConfiguration".casefold():
            from .ios_vpn_configuration import IosVpnConfiguration

            return IosVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSVpnConfiguration".casefold():
            from .mac_o_s_vpn_configuration import MacOSVpnConfiguration

            return MacOSVpnConfiguration()
        return AppleVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_vpn_connection_type import AppleVpnConnectionType
        from .device_configuration import DeviceConfiguration
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .ios_vpn_configuration import IosVpnConfiguration
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_on_demand_rule import VpnOnDemandRule
        from .vpn_provider_type import VpnProviderType
        from .vpn_proxy_server import VpnProxyServer
        from .vpn_server import VpnServer

        from .apple_vpn_connection_type import AppleVpnConnectionType
        from .device_configuration import DeviceConfiguration
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .ios_vpn_configuration import IosVpnConfiguration
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_on_demand_rule import VpnOnDemandRule
        from .vpn_provider_type import VpnProviderType
        from .vpn_proxy_server import VpnProxyServer
        from .vpn_server import VpnServer

        fields: dict[str, Callable[[Any], None]] = {
            "associatedDomains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_primitive_values(str)),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(AppleVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(KeyValuePair)),
            "disableOnDemandUserOverride": lambda n : setattr(self, 'disable_on_demand_user_override', n.get_bool_value()),
            "disconnectOnIdle": lambda n : setattr(self, 'disconnect_on_idle', n.get_bool_value()),
            "disconnectOnIdleTimerInSeconds": lambda n : setattr(self, 'disconnect_on_idle_timer_in_seconds', n.get_int_value()),
            "enablePerApp": lambda n : setattr(self, 'enable_per_app', n.get_bool_value()),
            "enableSplitTunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "excludeLocalNetworks": lambda n : setattr(self, 'exclude_local_networks', n.get_bool_value()),
            "excludedDomains": lambda n : setattr(self, 'excluded_domains', n.get_collection_of_primitive_values(str)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "includeAllNetworks": lambda n : setattr(self, 'include_all_networks', n.get_bool_value()),
            "loginGroupOrDomain": lambda n : setattr(self, 'login_group_or_domain', n.get_str_value()),
            "onDemandRules": lambda n : setattr(self, 'on_demand_rules', n.get_collection_of_object_values(VpnOnDemandRule)),
            "optInToDeviceIdSharing": lambda n : setattr(self, 'opt_in_to_device_id_sharing', n.get_bool_value()),
            "providerType": lambda n : setattr(self, 'provider_type', n.get_enum_value(VpnProviderType)),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(VpnProxyServer)),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "safariDomains": lambda n : setattr(self, 'safari_domains', n.get_collection_of_primitive_values(str)),
            "server": lambda n : setattr(self, 'server', n.get_object_value(VpnServer)),
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
        writer.write_collection_of_primitive_values("associatedDomains", self.associated_domains)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_bool_value("disableOnDemandUserOverride", self.disable_on_demand_user_override)
        writer.write_bool_value("disconnectOnIdle", self.disconnect_on_idle)
        writer.write_int_value("disconnectOnIdleTimerInSeconds", self.disconnect_on_idle_timer_in_seconds)
        writer.write_bool_value("enablePerApp", self.enable_per_app)
        writer.write_bool_value("enableSplitTunneling", self.enable_split_tunneling)
        writer.write_bool_value("excludeLocalNetworks", self.exclude_local_networks)
        writer.write_collection_of_primitive_values("excludedDomains", self.excluded_domains)
        writer.write_str_value("identifier", self.identifier)
        writer.write_bool_value("includeAllNetworks", self.include_all_networks)
        writer.write_str_value("loginGroupOrDomain", self.login_group_or_domain)
        writer.write_collection_of_object_values("onDemandRules", self.on_demand_rules)
        writer.write_bool_value("optInToDeviceIdSharing", self.opt_in_to_device_id_sharing)
        writer.write_enum_value("providerType", self.provider_type)
        writer.write_object_value("proxyServer", self.proxy_server)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_primitive_values("safariDomains", self.safari_domains)
        writer.write_object_value("server", self.server)
    

