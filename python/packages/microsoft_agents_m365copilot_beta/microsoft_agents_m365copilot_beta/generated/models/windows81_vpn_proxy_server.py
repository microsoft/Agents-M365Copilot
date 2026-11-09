from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vpn_proxy_server import VpnProxyServer

from .vpn_proxy_server import VpnProxyServer

@dataclass
class Windows81VpnProxyServer(VpnProxyServer, Parsable):
    """
    VPN Proxy Server.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows81VpnProxyServer"
    # Automatically detect proxy settings.
    automatically_detect_proxy_settings: Optional[bool] = None
    # Bypass proxy server for local address.
    bypass_proxy_server_for_local_address: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows81VpnProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows81VpnProxyServer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows81VpnProxyServer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vpn_proxy_server import VpnProxyServer

        from .vpn_proxy_server import VpnProxyServer

        fields: dict[str, Callable[[Any], None]] = {
            "automaticallyDetectProxySettings": lambda n : setattr(self, 'automatically_detect_proxy_settings', n.get_bool_value()),
            "bypassProxyServerForLocalAddress": lambda n : setattr(self, 'bypass_proxy_server_for_local_address', n.get_bool_value()),
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
        writer.write_bool_value("automaticallyDetectProxySettings", self.automatically_detect_proxy_settings)
        writer.write_bool_value("bypassProxyServerForLocalAddress", self.bypass_proxy_server_for_local_address)
    

