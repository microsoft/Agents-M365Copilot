from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .specified_captive_network_plugins import SpecifiedCaptiveNetworkPlugins
    from .vpn_service_exception_action import VpnServiceExceptionAction
    from .vpn_tunnel_configuration_type import VpnTunnelConfigurationType

@dataclass
class AppleVpnAlwaysOnConfiguration(AdditionalDataHolder, Parsable):
    """
    Always On VPN configuration for MacOS and iOS IKEv2
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Determine whether AirPrint service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
    air_print_exception_action: Optional[VpnServiceExceptionAction] = None
    # Specifies whether traffic from all captive network plugins should be allowed outside the vpn
    allow_all_captive_network_plugins: Optional[bool] = None
    # Determines whether traffic from the Websheet app is allowed outside of the VPN
    allow_captive_web_sheet: Optional[bool] = None
    # Determines whether all, some, or no non-native captive networking apps are allowed
    allowed_captive_network_plugins: Optional[SpecifiedCaptiveNetworkPlugins] = None
    # Determine whether Cellular service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
    cellular_exception_action: Optional[VpnServiceExceptionAction] = None
    # Specifies how often in seconds to send a network address translation keepalive package through the VPN
    nat_keep_alive_interval_in_seconds: Optional[int] = None
    # Enable hardware offloading of NAT keepalive signals when the device is asleep
    nat_keep_alive_offload_enable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of tunnels that will be present to the VPN client for configuration
    tunnel_configuration: Optional[VpnTunnelConfigurationType] = None
    # Allow the user to toggle the VPN configuration using the UI
    user_toggle_enabled: Optional[bool] = None
    # Determine whether voicemail service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
    voicemail_exception_action: Optional[VpnServiceExceptionAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppleVpnAlwaysOnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleVpnAlwaysOnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppleVpnAlwaysOnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .specified_captive_network_plugins import SpecifiedCaptiveNetworkPlugins
        from .vpn_service_exception_action import VpnServiceExceptionAction
        from .vpn_tunnel_configuration_type import VpnTunnelConfigurationType

        from .specified_captive_network_plugins import SpecifiedCaptiveNetworkPlugins
        from .vpn_service_exception_action import VpnServiceExceptionAction
        from .vpn_tunnel_configuration_type import VpnTunnelConfigurationType

        fields: dict[str, Callable[[Any], None]] = {
            "airPrintExceptionAction": lambda n : setattr(self, 'air_print_exception_action', n.get_enum_value(VpnServiceExceptionAction)),
            "allowAllCaptiveNetworkPlugins": lambda n : setattr(self, 'allow_all_captive_network_plugins', n.get_bool_value()),
            "allowCaptiveWebSheet": lambda n : setattr(self, 'allow_captive_web_sheet', n.get_bool_value()),
            "allowedCaptiveNetworkPlugins": lambda n : setattr(self, 'allowed_captive_network_plugins', n.get_object_value(SpecifiedCaptiveNetworkPlugins)),
            "cellularExceptionAction": lambda n : setattr(self, 'cellular_exception_action', n.get_enum_value(VpnServiceExceptionAction)),
            "natKeepAliveIntervalInSeconds": lambda n : setattr(self, 'nat_keep_alive_interval_in_seconds', n.get_int_value()),
            "natKeepAliveOffloadEnable": lambda n : setattr(self, 'nat_keep_alive_offload_enable', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tunnelConfiguration": lambda n : setattr(self, 'tunnel_configuration', n.get_enum_value(VpnTunnelConfigurationType)),
            "userToggleEnabled": lambda n : setattr(self, 'user_toggle_enabled', n.get_bool_value()),
            "voicemailExceptionAction": lambda n : setattr(self, 'voicemail_exception_action', n.get_enum_value(VpnServiceExceptionAction)),
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
        writer.write_enum_value("airPrintExceptionAction", self.air_print_exception_action)
        writer.write_bool_value("allowAllCaptiveNetworkPlugins", self.allow_all_captive_network_plugins)
        writer.write_bool_value("allowCaptiveWebSheet", self.allow_captive_web_sheet)
        writer.write_object_value("allowedCaptiveNetworkPlugins", self.allowed_captive_network_plugins)
        writer.write_enum_value("cellularExceptionAction", self.cellular_exception_action)
        writer.write_int_value("natKeepAliveIntervalInSeconds", self.nat_keep_alive_interval_in_seconds)
        writer.write_bool_value("natKeepAliveOffloadEnable", self.nat_keep_alive_offload_enable)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tunnelConfiguration", self.tunnel_configuration)
        writer.write_bool_value("userToggleEnabled", self.user_toggle_enabled)
        writer.write_enum_value("voicemailExceptionAction", self.voicemail_exception_action)
        writer.write_additional_data_value(self.additional_data)
    

