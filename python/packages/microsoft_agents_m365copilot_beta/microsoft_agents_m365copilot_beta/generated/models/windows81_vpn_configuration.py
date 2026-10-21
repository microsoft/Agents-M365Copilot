from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows81_vpn_proxy_server import Windows81VpnProxyServer
    from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
    from .windows_vpn_configuration import WindowsVpnConfiguration
    from .windows_vpn_connection_type import WindowsVpnConnectionType

from .windows_vpn_configuration import WindowsVpnConfiguration

@dataclass
class Windows81VpnConfiguration(WindowsVpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Windows 8.1 (and later) devices to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows81VpnConfiguration"
    # Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
    apply_only_to_windows81: Optional[bool] = None
    # Windows VPN connection type.
    connection_type: Optional[WindowsVpnConnectionType] = None
    # Enable split tunneling for the VPN.
    enable_split_tunneling: Optional[bool] = None
    # Login group or domain when connection type is set to Dell SonicWALL Mobile Connection.
    login_group_or_domain: Optional[str] = None
    # Proxy Server.
    proxy_server: Optional[Windows81VpnProxyServer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows81VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows81VpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81VpnConfiguration".casefold():
            from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

            return WindowsPhone81VpnConfiguration()
        return Windows81VpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows81_vpn_proxy_server import Windows81VpnProxyServer
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
        from .windows_vpn_configuration import WindowsVpnConfiguration
        from .windows_vpn_connection_type import WindowsVpnConnectionType

        from .windows81_vpn_proxy_server import Windows81VpnProxyServer
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
        from .windows_vpn_configuration import WindowsVpnConfiguration
        from .windows_vpn_connection_type import WindowsVpnConnectionType

        fields: dict[str, Callable[[Any], None]] = {
            "applyOnlyToWindows81": lambda n : setattr(self, 'apply_only_to_windows81', n.get_bool_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(WindowsVpnConnectionType)),
            "enableSplitTunneling": lambda n : setattr(self, 'enable_split_tunneling', n.get_bool_value()),
            "loginGroupOrDomain": lambda n : setattr(self, 'login_group_or_domain', n.get_str_value()),
            "proxyServer": lambda n : setattr(self, 'proxy_server', n.get_object_value(Windows81VpnProxyServer)),
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
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_bool_value("enableSplitTunneling", self.enable_split_tunneling)
        writer.write_str_value("loginGroupOrDomain", self.login_group_or_domain)
        writer.write_object_value("proxyServer", self.proxy_server)
    

