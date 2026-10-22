from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .vpn_server import VpnServer
    from .windows10_vpn_configuration import Windows10VpnConfiguration
    from .windows81_vpn_configuration import Windows81VpnConfiguration
    from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsVpnConfiguration(DeviceConfiguration, Parsable):
    """
    Windows VPN configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsVpnConfiguration"
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
    custom_xml: Optional[bytes] = None
    # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
    servers: Optional[list[VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsVpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10VpnConfiguration".casefold():
            from .windows10_vpn_configuration import Windows10VpnConfiguration

            return Windows10VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81VpnConfiguration".casefold():
            from .windows81_vpn_configuration import Windows81VpnConfiguration

            return Windows81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81VpnConfiguration".casefold():
            from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

            return WindowsPhone81VpnConfiguration()
        return WindowsVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .vpn_server import VpnServer
        from .windows10_vpn_configuration import Windows10VpnConfiguration
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

        from .device_configuration import DeviceConfiguration
        from .vpn_server import VpnServer
        from .windows10_vpn_configuration import Windows10VpnConfiguration
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "customXml": lambda n : setattr(self, 'custom_xml', n.get_bytes_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(VpnServer)),
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
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_bytes_value("customXml", self.custom_xml)
        writer.write_collection_of_object_values("servers", self.servers)
    

